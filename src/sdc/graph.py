
from sdc.gibbs import gibbs_m_pa, gibbs_rl_pa, gibbs_assoc
from sdc.tile import Tile, NullTile

from collections import defaultdict

from typing import Callable, Dict, Generator, List, Tuple




class SDCGraph:

    def __init__(self, tiles: List[List[Tile]]):
        self.tiles = tiles


        self._processed_tiles: List[List[Tile]] = []

        # add NullTile - representing unoccupied position
        for l in range(len(tiles)):
            self._processed_tiles.append([NullTile(l)] + tiles[l])

        # add NullTile to end - acting as a sentinel - used in shortest path
        self._processed_tiles.append([NullTile(len(tiles))])


        self._edge_weights: Dict[Tile, Dict[Tile, Callable]] = defaultdict(dict)
        self._node_weights: Dict[Tile, Callable] = {}

        self._nodes: List[Tile] = []

        # preprocess the node / edge weights
        for v in self._processed_tiles[0]:
            self._node_weights[v] = gibbs_m_pa(v)
            self._nodes.append(v)

        for l in range(1, len(self._processed_tiles)):
            for u in self._processed_tiles[l - 1]:
                for v in self._processed_tiles[l]:
                    self._edge_weights[u][v] = gibbs_rl_pa(u, v)
                    self._node_weights[v]    = gibbs_m_pa(v)
                    self._nodes.append(v)



    def get_tileset(self) -> List[List[Tile]]:
        return self.tiles

    def get_nodes(self) -> List[Tile]:
        return self._nodes

    def get_layer(self, layer: int) -> List[Tile]:
        if layer == len(self._processed_tiles):
            raise ValueError("outside the range of layers")
        return self._processed_tiles[layer]



    def get_node_weight(self, tile: Tile, T: float) -> float:
        return self._node_weights[tile](T)

    def get_edge_weight(self, left: Tile, right: Tile, T: float) -> float:
        return self._edge_weights[left][right](T)

    def get_outgoing_edges(self, layer: int) -> Generator[Tuple[Tile, Tile]]:
        for u in self.get_layer(layer):
            for v in self.get_layer(layer + 1):
                yield (u, v)



    def minimum_free_energy(self, source: Tile, T: float) -> Tuple[float, List[Tile]]:
        if source.get_layer() != 0 or source not in self.tiles[0]:
            raise ValueError("source tile should be from layer 0")

        pred = {}
        path = []

        dist = {n: float('inf') for n in self.get_nodes()}
        dist[source] = 0

        for l in range(len(self._processed_tiles) - 1):
            for u, v in self.get_outgoing_edges(l):
                uv = self.get_edge_weight(u, v, T)
                if dist[v] > dist[u] + uv:
                    dist[v] = dist[u] + uv
                    pred[v] = u

        node = self._processed_tiles[-1][0]
        mfe  = dist[node]

        while node in pred:
            node = pred[node]
            mfe += self.get_node_weight(node, T)
            mfe += gibbs_assoc(T)
            path.append(node)

        return mfe, path[::-1]



    def configuration_free_energy(self, configuration: Tuple[int, ...], T: float) -> float:
        N = len(self.tiles)
        M = len(configuration)

        if M != len(self.tiles):
            raise ValueError("configuration should be of length {N}")

        E = 0

        for i in range(M):
            E += self.get_node_weight(self._processed_tiles[i][configuration[i]], T)
            E += gibbs_assoc(T)

        for i in range(1, M):
            E += self.get_edge_weight(self._processed_tiles[i - 1][configuration[i - 1]], self._processed_tiles[i][configuration[i]], T)

        return E

