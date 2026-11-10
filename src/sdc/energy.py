
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc, beta
from sdc.tile import Tile

from typing import Dict, List, Tuple

import itertools
import math




def minimum_free_energy(tiles: List[List[Tile]], T: float) -> float:
    """

        calculate the Minimum Free Energy of the tileset

        Parameters
        ----------
        tiles: List[List[Tile]]
            the tileset of the computation
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Minimum Free Energy of the tileset

    """
    N = len(tiles)
    K = max(len(t) for t in tiles)

    M_curr: List[float] = [0] * K

    for j in range(len(tiles[0])):
        M_curr[j] = gibbs_m(tiles[0][j], T) + gibbs_assoc(T)

    for i in range(1, N):
        M_prev = M_curr
        M_curr = [0] * K

        for j in range(len(tiles[i])):
            M_curr[j] = gibbs_m(tiles[i][j], T) + gibbs_assoc(T) + min(M_prev[m] + gibbs_rl(tiles[i - 1][m], tiles[i][j], T) for m in range(len(tiles[i - 1])))

    return min(M_curr)




def minimum_free_energy_configuration(tiles: List[List[Tile]], T: float) -> List[Tile]:
    """

        finds the configuration with the Minimum Free Energy of the provided tileset

        Parameters
        ----------
        tiles: List[List[Tile]]
            the tileset of the computation
        T: float
            the temperature in Kelvin

        Returns
        -------
        List[Tile]
            the configuration with the Minimum Free Energy of the provided tileset

    """
    N = len(tiles)
    K = max(len(t) for t in tiles)

    M: List[List[float]] = [[0 for _ in range(K)] for _ in range(N)]

    for j in range(len(tiles[0])):
        M[0][j] = gibbs_m(tiles[0][j], T) + gibbs_assoc(T)

    for i in range(1, N):
        for j in range(len(tiles[i])):
            M[i][j] = gibbs_m(tiles[i][j], T) + gibbs_assoc(T) + min(M[i - 1][m] + gibbs_rl(tiles[i - 1][m], tiles[i][j], T) for m in range(len(tiles[i - 1])))

    return [tiles[i][M[i].index(min(M[i]))] for i in range(len(M))]




def partition_function(tiles: List[List[Tile]], T: float) -> float:
    """

        calculate the Partition Function of the tileset

        Parameters
        ----------
        tiles: List[List[Tile]]
            the tileset of the computation
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Partition Function of the tileset

    """
    N = len(tiles)
    K = max(len(t) for t in tiles)

    Z_curr: List[float] = [0] * K
    Z_prev: List[float] = [0] * K
    Z_ptmp: float = 0

    Z = 1

    for j in range(len(tiles[0])):
        Z_curr[j] = math.exp( -beta(T) * (gibbs_m(tiles[0][j], T) + gibbs_assoc(T)) )

        Z += Z_curr[j]

    for i in range(1, N):
        Z_ptmp += sum(Z_prev)

        Z_prev  = Z_curr
        Z_curr  = [0] * K

        for j in range(len(tiles[i])):
            Z_curr[j] += 1
            for m in range(len(tiles[i - 1])):
                Z_curr[j] += math.exp( -beta(T) * gibbs_rl(tiles[i - 1][m], tiles[i][j], T) ) * Z_prev[m]
            Z_curr[j] += Z_ptmp
            Z_curr[j] *= math.exp( -beta(T) * (gibbs_m(tiles[i][j], T) + gibbs_assoc(T)) )

            Z += Z_curr[j]

    return Z




def minimum_free_energy_probability(tiles: List[List[Tile]], T: float) -> float:
    """

        finds the probability for the configuration of the Minimum Free Energy of the provided tileset

        Parameters
        ----------
        tiles: List[List[Tile]]
            the tileset of the computation
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the probability for the configuration of the Minimum Free Energy of the provided tileset

    """
    return math.exp( -beta(T) * minimum_free_energy(tiles, T) ) / partition_function(tiles, T)




def free_energies(tiles: List[List[Tile]], T: float) -> Tuple[Dict[Tuple[int, ...], float], float]:
    """

        creates a dictionary of Boltzmann probabilities associated
        with each configuration, along with the Partition Function,
        of the provided tileset

        NOTE: this function has exponential time complexity -
        exponential in the number of positions - do not use!!!

        Parameters
        ----------
        tiles: List[List[Tile]]
            the tileset of the computation
        T: float
            the temperature in Kelvin

        Returns
        -------
        Dict[Tuple[int, ...], float]
            a dictionary of free energies keyed by configuration
        float
            the Partition Function of the tileset

    """
    N = len(tiles)
    C = {}
    Z = 0

    for c in itertools.product(*[range(len(t) + 1) for t in tiles]):
        E = 1

        for i in range(N):
            if 0 < c[i]:
                E *= math.exp( -beta(T) * (gibbs_m(tiles[i][c[i] - 1], T) + gibbs_assoc(T)) )

        for i in range(1, N):
            if 0 < c[i - 1] and 0 < c[i]:
                E *= math.exp( -beta(T) * gibbs_rl(tiles[i - 1][c[i - 1] - 1], tiles[i][c[i] - 1], T) )

        C[c] = E
        Z   += E

    for c in C:
        C[c] /= Z

    return C, Z
