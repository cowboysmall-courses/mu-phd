
from sdc.tile import Tile, NullTile

from typing import Dict, List



class Scaffold:

    def __init__(self, positions: List[str]):
        self.positions = positions
        self.count = len(positions)

        self._index: Dict[str, int] = {p:i for i, p in enumerate(self.positions)}
        self._bindings: Dict[int, Tile] = {i:NullTile(i) for i in range(self.count)}



    def get_positions(self) -> List[str]:
        """

            get the positions on the scaffold

            Returns
            -------
            List[str]
                the positions on the scaffold

        """
        return self.positions

    def get_count(self) -> int:
        """

            get the number of positions on the scaffold

            Returns
            -------
            int
                the number of positions of the scaffold

        """
        return self.count



    def get_position_index(self, position: str) -> int:
        """

            get the index of the position on the scaffold

            Returns
            -------
            int
                the index of the position on the scaffold

        """
        return self._index[position]

    def get_bound_tiles(self) -> List[Tile]:
        """

            get a list of the bound tiles on the scaffold

            Returns
            -------
            List[Tile]
                a list of the bound tiles on the scaffold

        """
        return [self._bindings[i] for i in range(self.count)]



    def bind(self, tile: Tile) -> None:
        """

            binds the tile to the scaffold

            Parameters
            ----------
            tile: Tile
                the tile to bind to the scaffold

        """
        position = self._index[tile.get_middle_complement()]
        self._bindings[position] = tile

    def unbind(self, tile: Tile) -> None:
        """

            unbinds the tile from the scaffold

            Parameters
            ----------
            tile: Tile
                the tile to unbind from the scaffold

        """
        position = self._index[tile.get_middle_complement()]
        self._bindings[position] = NullTile(position)

    def replace(self, tile: Tile) -> Tile | None:
        """

            replaces the tile within the scaffold, returning the replaced tile

            Parameters
            ----------
            tile: Tile
                the tile to replace the existing tile with

            Returns
            -------
            Tile
                the tile replaced

        """
        position = self._index[tile.get_middle_complement()]
        current = self._bindings[position]
        self._bindings[position] = tile
        return current



    def is_position_free(self, tile: Tile) -> bool:
        """

            checks if the position within the scaffold is free

            Parameters
            ----------
            index: int
                the position within the scaffold

            Returns
            -------
            bool
                whether the position within the scaffold is free

        """
        position = self._index[tile.get_middle_complement()]
        return isinstance(self._bindings[position], NullTile)

    def is_position_taken(self, tile: Tile) -> bool:
        """

            checks if the position within the scaffold is taken

            Parameters
            ----------
            index: int
                the position within the scaffold

            Returns
            -------
            bool
                whether the position within the scaffold is taken

        """
        return not self.is_position_free(tile)



    def __repr__(self):
        return "-".join(self.positions)

    def __eq__(self, other):
        if not isinstance(other, Scaffold):
            return NotImplemented
        return (self.positions, self.count) == (other.positions, other.count)

    def __hash__(self):
        return hash((self.positions, self.count))







