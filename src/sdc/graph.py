
from sdc.gibbs import gibbs_m, gibbs_rl, gibbs_assoc
from sdc.tile import Tile

from collections import defaultdict

from typing import Callable, Dict, List, Tuple

import functools


class SDCGraph:

    def __init__(self, tiles: Dict[int, List[Tile]]):
        self.tiles   = tiles
        self.l_count = len(tiles)

        self._edge_weights: Dict[Tile, Dict[Tile, Callable]] = defaultdict(dict)
        self._node_weights: Dict[Tile, Callable] = {}

        # preprocess the node / edge weights
        for u in self.tiles[0]:
            self._node_weights[u] = gibbs_m_pa(u)

        for i in range(self.l_count - 1):
            for u in self.tiles[i]:
                for v in self.tiles[i + 1]:
                    self._edge_weights[u][v] = gibbs_rl_pa(u, v)
                    self._node_weights[v]    = gibbs_m_pa(v)



    def get_tiles(self) -> Dict[int, List[Tile]]:
        return self.tiles

    def get_layer_count(self) -> int:
        return self.l_count



    def get_node_weight(self, tile: Tile, T: float) -> float:
        return self._node_weights[tile](T)

    def get_edge_weight(self, left: Tile, right: Tile, T: float) -> float:
        return self._edge_weights[left][right](T)

    def get_next(self, tile: Tile) -> List[Tile]:
        if tile.get_layer() == len(self.tiles) - 1:
            raise ValueError("tile from last layer")
        return self.tiles[tile.get_layer() + 1]




    def shortest_path(self, source: Tile, T: float) -> Tuple[float, List[Tile]]:
        if source.get_layer() != 0 or source not in self.tiles[0]:
            raise ValueError("source tile should be from layer 0")

        # local copy of tiles and layer count
        tiles   = dict(self.tiles)
        l_count = self.l_count

        # dummy / sentinel used in shortest path
        dummy = Tile(l_count, "", layout = (0, 0, 0))

        # add dumy / sentinel to edge and node weights
        for v in tiles[l_count - 1]:
            self._edge_weights[v][dummy] = gibbs_rl_pa(v, dummy)
            self._node_weights[dummy]    = gibbs_m_pa(dummy)

        # add dummy / sentinel to tiles and increment layer count
        tiles[l_count] = [dummy]
        l_count += 1

        # distance map with
        dist = {n: float('inf') for n in self._node_weights}
        dist[source] = 0

        # predecessor map and path list
        pred = {}
        path = []

        for i in range(l_count - 1):
            for u in tiles[i]:
                for v in tiles[i + 1]:
                    uv = self.get_edge_weight(u, v, T)
                    # relax edge u -> v
                    if dist[v] > dist[u] + uv:
                        dist[v] = dist[u] + uv
                        pred[v] = u

        # sum free energy + construct favourable path
        node = dummy
        mfe  = dist[dummy]

        while node in pred:
            node = pred[node]
            path.append(node)
            mfe += self.get_node_weight(node, T) + gibbs_assoc(T)

        return mfe, path[::-1]



# gibbs_m - partial application
def gibbs_m_pa(tile:Tile):
    @functools.cache
    def gibbs_m_T(T: float):
        return gibbs_m(tile, T)
    return gibbs_m_T

# gibbs_rl - partial application
def gibbs_rl_pa(l:Tile, r: Tile):
    @functools.cache
    def gibbs_rl_T(T: float):
        return gibbs_rl(l, r, T)
    return gibbs_rl_T
