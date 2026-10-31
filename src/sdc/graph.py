
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile

from collections import defaultdict

from typing import Callable, Dict, List, Tuple

import functools


class SDCGraph:

    def __init__(self, tiles: List[List[Tile]]):
        self.tiles = tiles

        # add dummy / sentinel - used in shortest path - to tiles
        self._dummy = Tile(len(tiles), "", layout = (0, 0, 0))
        tiles.append([self._dummy])

        self._edge_weights: Dict[Tile, Dict[Tile, Callable]] = defaultdict(dict)
        self._node_weights: Dict[Tile, Callable] = {}

        # preprocess the node / edge weights
        for u in tiles[0]:
            self._node_weights[u] = gibbs_m_pa(u)

        for l in range(len(tiles) - 1):
            for u in tiles[l]:
                for v in tiles[l + 1]:
                    self._edge_weights[u][v] = gibbs_rl_pa(u, v)
                    self._node_weights[v]    = gibbs_m_pa(v)



    def get_tiles(self) -> List[List[Tile]]:
        return self.tiles[:-1]

    def get_layer(self, layer: int) -> List[Tile]:
        if layer == len(self.tiles):
            raise ValueError("outside the range of layers")
        return self.tiles[layer]



    def get_node_weight(self, tile: Tile, T: float) -> float:
        return self._node_weights[tile](T)

    def get_edge_weight(self, left: Tile, right: Tile, T: float) -> float:
        return self._edge_weights[left][right](T)



    def shortest_path(self, source: Tile, T: float) -> Tuple[float, List[Tile]]:
        if source.get_layer() != 0 or source not in self.tiles[0]:
            raise ValueError("source tile should be from layer 0")

        # distance map with
        dist = {n: float('inf') for n in self._node_weights}
        dist[source] = 0

        # predecessor map and path list
        pred = {}
        path = []

        for l in range(len(self.tiles) - 1):
            for u in self.get_layer(l):
                for v in self.get_layer(l + 1):
                    uv = self.get_edge_weight(u, v, T)
                    # relax edge u -> v
                    if dist[v] > dist[u] + uv:
                        dist[v] = dist[u] + uv
                        pred[v] = u

        # sum free energy + construct favourable path
        node = self._dummy
        mfe  = dist[self._dummy]

        while node in pred:
            node = pred[node]
            mfe += self.get_node_weight(node, T) + gibbs_assoc(T)
            path.append(node)

        return mfe, path[::-1]



# gibbs_m - partial application
def gibbs_m_pa(tile:Tile):
    @functools.cache
    def gibbs_m_T(T: float):
        return 0 if tile.middle() == "" else gibbs_m(tile, T)
    return gibbs_m_T

# gibbs_rl - partial application
def gibbs_rl_pa(l:Tile, r: Tile):
    @functools.cache
    def gibbs_rl_T(T: float):
        return 0 if r.left() == "" else gibbs_rl(l, r, T)
    return gibbs_rl_T
