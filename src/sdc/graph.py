
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile

from collections import defaultdict, deque

from typing import Callable, Dict, List

import functools


class SDCGraph:

    def __init__(self, tiles: Dict[int, List[Tile]]):
        self._tiles = tiles
        self._nodes = []
        self._edges = []

        self._edge_weights: Dict[Tile, Dict[Tile, Callable]] = defaultdict(dict)
        self._node_weights: Dict[Tile, Callable] = {}

        for i in range(len(tiles) - 1):
            for u in tiles[i]:
                self._nodes.append(u)
                self._node_weights[u] = gibbs_m_c(u)
                for v in tiles[i + 1]:
                    self._edges.append((u, v))
                    self._edge_weights[u][v] = gibbs_rl_c(u, v)
                    self._nodes.append(v)
                    self._node_weights[v] = gibbs_m_c(v)



    def get_node_weight(self, tile: Tile, T: float) -> float:
        return self._node_weights[tile](T)

    def get_edge_weight(self, left: Tile, right: Tile, T: float) -> float:
        return self._edge_weights[left][right](T)

    def get_next(self, tile: Tile) -> List[Tile]:
        return list(self._edge_weights[tile].keys())



    def shortest_path(self, tile: Tile, T: float) -> Dict[Tile, float]:
        dist = {n: self._node_weights[n](T) for n in self._nodes}

        for u in self._edge_weights:
            for v in self._edge_weights[u]:
                uv = self._edge_weights[u][v](T)
                if dist[u] + uv < dist[v]:
                    dist[v] = dist[u] + uv

        return dist








def gibbs_m_c(tile:Tile):
    @functools.cache
    def inner(T: float):
        return gibbs_m(tile, T)
    return inner

def gibbs_rl_c(l:Tile, r: Tile):
    @functools.cache
    def inner(T: float):
        return gibbs_rl(l, r, T)
    return inner

