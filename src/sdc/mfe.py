
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile
from sdc import R_j

from typing import List

import math


def target_configuration_probability(tiles: List[List[Tile]], T: float) -> float:
    return math.exp( -(minimum_free_energy(tiles, T)) / (R_j * T) ) / partition_function(tiles, T)


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
        M_curr[j] = gibbs_m(tiles[0][j], T)

    for i in range(1, N):
        M_prev = M_curr
        M_curr = [0] * K

        for j in range(len(tiles[i])):
            M_temp = []

            for m in range(len(tiles[i - 1])):
                M_temp.append(M_prev[m] + gibbs_rl(tiles[i - 1][m], tiles[i][j], T))

            M_curr[j] = min(M_temp) + gibbs_m(tiles[i][j], T) + gibbs_assoc(T)

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
        M[0][j] = gibbs_m(tiles[0][j], T)

    for i in range(1, N):
        for j in range(len(tiles[i])):
            M_temp = []

            for k in range(len(tiles[i - 1])):
                M_temp.append(M[i - 1][k] + gibbs_rl(tiles[i - 1][k], tiles[i][j], T))

            M[i][j] = min(M_temp) + gibbs_m(tiles[i][j], T) + gibbs_assoc(T)

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
    S = 0
    Z = 1

    Z_curr: List[float] = [0] * K
    Z_prev: List[float] = [0] * K

    for j in range(len(tiles[0])):
        Z_curr[j] = math.exp( -(gibbs_m(tiles[0][j], T) + gibbs_assoc(T)) / (R_j * T) )
        Z += Z_curr[j]

    for i in range(1, N):
        S += sum(Z_prev)

        Z_prev = Z_curr
        Z_curr = [0] * K

        for j in range(len(tiles[i])):
            Z_curr[j] = math.exp( -(gibbs_m(tiles[i][j], T) + gibbs_assoc(T)) / (R_j * T) )

            for m in range(len(tiles[i - 1])):
                Z_curr[j] += math.exp( -gibbs_rl(tiles[i - 1][m], tiles[i][j], T) / (R_j * T) ) * Z_prev[m]

            Z_curr[j] += S

            Z += Z_curr[j]

    return Z
