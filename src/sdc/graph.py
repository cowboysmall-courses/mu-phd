
from sdc.gibbs import gibbs_m_pa, gibbs_rl_pa, gibbs_assoc
from sdc.tile import Tile, NullTile

from collections import defaultdict

from typing import Callable, Dict, Generator, List, Tuple



class SDCGraph:

    def __init__(self, tileset: List[List[Tile]]):
        self.tileset   = tileset
        self.positions = len(tileset)

        # preprocess tileset
        self._processed_tileset: List[List[Tile]] = []
        # add NullTile - representing unoccupied position
        for l in range(self.positions):
            self._processed_tileset.append([NullTile(l)] + tileset[l])
        # add NullTile to layer at end - acting as a sentinel - used in shortest path
        self._processed_tileset.append([NullTile(self.positions)])

        self._edge_weights: Dict[Tile, Dict[Tile, Callable]] = defaultdict(dict)
        self._node_weights: Dict[Tile, Callable] = {}
        self._nodes: List[Tile] = []

        # preprocess the node / edge weights
        for v in self._processed_tileset[0]:
            self._node_weights[v] = gibbs_m_pa(v)
            self._nodes.append(v)

        for l in range(1, len(self._processed_tileset)):
            for u in self._processed_tileset[l - 1]:
                for v in self._processed_tileset[l]:
                    self._edge_weights[u][v] = gibbs_rl_pa(u, v)
                    self._node_weights[v]    = gibbs_m_pa(v)
                    self._nodes.append(v)



    def get_tileset(self) -> List[List[Tile]]:
        return self.tileset

    def get_nodes(self) -> List[Tile]:
        return self._nodes



    def _get_layer(self, layer: int) -> List[Tile]:
        if layer == len(self._processed_tileset):
            raise ValueError("outside the range of layers")

        return self._processed_tileset[layer]



    def get_node_weight(self, tile: Tile, T: float) -> float:
        return self._node_weights[tile](T)

    def get_edge_weight(self, left: Tile, right: Tile, T: float) -> float:
        return self._edge_weights[left][right](T)

    def get_outgoing_edges(self, layer: int) -> Generator[Tuple[Tile, Tile]]:
        for u in self._get_layer(layer):
            for v in self._get_layer(layer + 1):
                yield (u, v)



    def minimum_free_energy(self, source: Tile, T: float) -> Tuple[float, List[Tile]]:
        # if source.get_layer() != 0 or source not in self.tileset[0]:
        if source not in self.tileset[0]:
            raise ValueError("source tile should be from layer 0")

        dist = {n: float('inf') for n in self.get_nodes()}
        dist[source] = 0

        pred = {}

        for l in range(self.positions):
            for u, v in self.get_outgoing_edges(l):
                uv = self.get_edge_weight(u, v, T)
                if dist[v] > dist[u] + uv:
                    dist[v] = dist[u] + uv
                    pred[v] = u

        V = self._processed_tileset[-1][0]
        E = dist[V]

        P = []
        while V in pred:
            V = pred[V]

            E += self.get_node_weight(V, T)
            E += gibbs_assoc(T)

            P.append(V)

        return E, P[::-1]



    def configuration_free_energy(self, configuration: Tuple[int, ...], T: float) -> float:
        N = len(configuration)

        if N != self.positions:
            raise ValueError(f"configuration should be of length {self.positions}")

        return self.tiles_free_energy([self._processed_tileset[i][configuration[i]] for i in range(N)], T)



    def tiles_free_energy(self, tiles: List[Tile], T: float) -> float:
        N = len(tiles)

        if N != self.positions:
            raise ValueError(f"tiles should be of length {self.positions}")

        E = 0

        for i in range(N):
            E += self.get_node_weight(tiles[i], T)
            E += gibbs_assoc(T)

        for i in range(1, N):
            E += self.get_edge_weight(tiles[i - 1], tiles[i], T)

        return E

