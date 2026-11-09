
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile

from typing import List


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

    for i in range(N):
        M_prev = M_curr
        M_curr = [0] * K

        for j in range(len(tiles[i])):
            M_curr[j] = gibbs_m(tiles[i][j], T) + gibbs_assoc(T)

            if i > 0:
                M_curr[j] += min(M_prev[m] + gibbs_rl(tiles[i - 1][m], tiles[i][j], T) for m in range(len(tiles[i - 1])))

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

    for i in range(N):
        for j in range(len(tiles[i])):
            M[i][j] = gibbs_m(tiles[i][j], T) + gibbs_assoc(T)

            if i > 0:
                M[i][j] += min(M[i - 1][m] + gibbs_rl(tiles[i - 1][m], tiles[i][j], T) for m in range(len(tiles[i - 1])))

    return [tiles[i][M[i].index(min(M[i]))] for i in range(len(M))]
