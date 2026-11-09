
from collections import defaultdict

from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile
from sdc import R_j

from typing import Dict, List, Tuple

import itertools
import math


def partition_function_database(tiles: List[List[Tile]], T: float) -> Tuple[Dict[Tuple[int, ...], float], float]:
    N = len(tiles)
    C = {}
    Z = 0

    for c in itertools.product(*[range(len(t) + 1) for t in tiles]):
        E = 0

        for i in range(N):
            if 0 < c[i]:
                E += -(gibbs_m(tiles[i][c[i] - 1], T) + gibbs_assoc(T))

        for i in range(1, N):
            if 0 < c[i - 1] and 0 < c[i]:
                E += -gibbs_rl(tiles[i - 1][c[i - 1] - 1], tiles[i][c[i] - 1], T)

        C[c] = math.exp(E / (R_j * T))
        Z   += C[c]

    return C, Z



def partition_function_database_2(tiles: List[List[Tile]], T: float) -> Tuple[Dict[Tuple[int, ...], float], float]:
    N = len(tiles)
    C = {}
    Z = 0

    for c in itertools.product(*[range(len(t) + 1) for t in tiles]):
        E = 1

        for i in range(N):
            if 0 < c[i]:
                E *= math.exp( -(gibbs_m(tiles[i][c[i] - 1], T) + gibbs_assoc(T)) / (R_j * T))

        for i in range(1, N):
            if 0 < c[i - 1] and 0 < c[i]:
                E *= math.exp( -gibbs_rl(tiles[i - 1][c[i - 1] - 1], tiles[i][c[i] - 1], T) / (R_j * T))

        C[c] = E
        Z   += E

    return C, Z



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

    P = 0
    Z = 1

    for j in range(len(tiles[0])):
        Z_curr[j] = math.exp( -(gibbs_m(tiles[0][j], T) + gibbs_assoc(T)) / (R_j * T) )
        Z += Z_curr[j]

    for i in range(1, N):
        P += sum(Z_prev)

        Z_prev  = Z_curr
        Z_curr  = [0] * K

        for j in range(len(tiles[i])):
            Z_temp = 0
            for m in range(len(tiles[i - 1])):
                Z_temp += math.exp( -gibbs_rl(tiles[i - 1][m], tiles[i][j], T) / (R_j * T) ) * Z_prev[m]
            Z_curr[j] = (1 + Z_temp + P) * math.exp( -(gibbs_m(tiles[i][j], T) + gibbs_assoc(T)) / (R_j * T) )

            Z += Z_curr[j]

    return Z
