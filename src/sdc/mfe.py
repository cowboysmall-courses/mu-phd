
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile
from sdc import R_j

from typing import Dict, List

import math


def minimum_free_energy(tiles: Dict[int, List[Tile]], T: float) -> float:
    N = len(tiles)
    K = max(len(t) for t in tiles.values())

    M_curr: List[float] = [0] * K

    for j in range(len(tiles[0])):
        M_curr[j] = gibbs_m(tiles[0][j], T)

    for i in range(1, N):
        M_prev = M_curr
        M_curr = [0] * K

        for j in range(len(tiles[i])):
            M_temp = []

            for k in range(len(tiles[i - 1])):
                M_temp.append(M_prev[k] + gibbs_rl(tiles[i - 1][k], tiles[i][j], T))

            M_curr[j] = min(M_temp) + gibbs_m(tiles[i][j], T) + gibbs_assoc(T)

    return min(M_curr)



def minimum_free_energy_configuration(tiles: Dict[int, List[Tile]], T: float) -> List[Tile]:
    N = len(tiles)
    K = max(len(t) for t in tiles.values())
    C = []

    M_curr: List[float] = [0] * K

    for j in range(len(tiles[0])):
        M_curr[j] = gibbs_m(tiles[0][j], T)

    C.append(tiles[0][M_curr.index(min(M_curr))])

    for i in range(1, N):
        M_prev = M_curr
        M_curr = [0] * K

        for j in range(len(tiles[i])):
            M_temp = []

            for k in range(len(tiles[i - 1])):
                M_temp.append(M_prev[k] + gibbs_rl(tiles[i - 1][k], tiles[i][j], T))

            M_curr[j] = min(M_temp) + gibbs_m(tiles[i][j], T) + gibbs_assoc(T)

        C.append(tiles[i][M_curr.index(min(M_curr))])

    return C



def partition_function(tiles: Dict[int, List[Tile]], T: float) -> float:
    N = len(tiles)
    K = max(len(t) for t in tiles.values())

    Z_curr: List[float] = [0] * K
    Z_prev: List[float] = [0] * K

    Z_conf = 1
    S_prev = 0

    for j in range(len(tiles[0])):
        Z_curr[j] = math.exp( -(gibbs_m(tiles[0][j], T) + gibbs_assoc(T)) / (R_j * T) )

    for i in range(1, N):
        S_prev += sum(Z_prev)
        Z_prev = Z_curr
        Z_curr = [0] * K

        for j in range(len(tiles[i])):
            Z_curr[j] = S_prev + math.exp( -(gibbs_m(tiles[i][j], T) + gibbs_assoc(T)) / (R_j * T) )

            for k in range(len(tiles[i - 1])):
                Z_curr[j] += math.exp( -gibbs_rl(tiles[i - 1][k], tiles[i][j], T) / (R_j * T) ) * Z_prev[k]

            Z_conf += Z_curr[j]

    return Z_conf



def mu(tile: Tile, T: float) -> float:
    return R_j * T * math.log(tile.get_concentration() / u_0)
