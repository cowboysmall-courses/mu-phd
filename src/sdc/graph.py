
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile

from collections import defaultdict

from typing import Callable, Dict, List, Tuple

import functools


class SDCGraph:

    def __init__(self, tiles: Dict[int, List[Tile]]):
        self._tiles  = tiles
        self._layers = len(tiles)
        self._nodes  = []
        self._edges  = []

        self._edge_weights: Dict[Tile, Dict[Tile, Callable]] = defaultdict(dict)
        self._node_weights: Dict[Tile, Callable] = {}

        for i in range(self._layers - 1):
            for u in tiles[i]:
                self._nodes.append(u)
                self._node_weights[u] = gibbs_m_pa(u)
                for v in tiles[i + 1]:
                    self._edges.append((u, v))
                    self._edge_weights[u][v] = gibbs_rl_pa(u)(v)
                    self._nodes.append(v)
                    self._node_weights[v] = gibbs_m_pa(v)



    def get_node_weight(self, tile: Tile, T: float) -> float:
        return self._node_weights[tile](T)

    def get_edge_weight(self, left: Tile, right: Tile, T: float) -> float:
        return self._edge_weights[left][right](T)

    def get_next(self, tile: Tile) -> List[Tile]:
        return list(self._edge_weights[tile].keys())



    def shortest_path(self, T: float) -> Tuple[float, List[Tile]]:
        dist = {n: float('inf') for n in self._nodes}
        dist[self._tiles[0][0]] = 0

        pred = {}
        path = []

        for i in range(self._layers - 1):
            for u in self._tiles[i]:
                for v in self._tiles[i + 1]:
                    uv = self._edge_weights[u][v](T)
                    if dist[u] + uv < dist[v]:
                        dist[v] = dist[u] + uv
                        pred[v] = u

        mfe, node = min([(dist[t], t) for t in self._tiles[self._layers - 1]])

        path.append(node)
        mfe += self._node_weights[node](T)

        while node in pred:
            node = pred[node]
            path.append(node)
            mfe += self._node_weights[node](T) + gibbs_assoc(T)

        return mfe, path[::-1]




def gibbs_m_pa(tile:Tile):
    @functools.cache
    def gibbs_m_T(T: float):
        return gibbs_m(tile, T)
    return gibbs_m_T

def gibbs_rl_pa(l:Tile):
    def gibbs_rl_r(r: Tile):
        @functools.cache
        def gibbs_rl_T(T: float):
            return gibbs_rl(l, r, T)
        return gibbs_rl_T
    return gibbs_rl_r

