
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



    def is_free(self, tile: Tile) -> bool:
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

    def is_taken(self, tile: Tile) -> bool:
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
        return not self.is_free(tile)






class ScaffoldManager:

    def __init__(self, strand: str, position_size: int = 24, concentration: int = 1):
        self.strand = strand
        self.position_size = position_size
        self.concentration = concentration

        self._scaffolds: List[Scaffold] = []
        self._current: int = 0

        strand = strand.replace(" ", "")[::-1]
        for _ in range(self.concentration):
            self._scaffolds.append(Scaffold([strand[i:i + self.position_size] for i in range(0, len(strand), self.position_size)]))



    def get_strand(self) -> str:
        """

            get the underlying strand of the scaffold

            Returns
            -------
            str
                the underlying strand of the scaffold

        """
        return self.strand

    def get_position_size(self) -> int:
        """

            get the position size of the scaffold

            Returns
            -------
            int
                the position size of the scaffold

        """
        return self.position_size

    def get_concentration(self) -> int:
        """

            get the concentration of the scaffold

            Returns
            -------
            int
                the position size of the scaffold

        """
        return self.concentration



    def next(self) -> Scaffold:
        """

            retrieves the next scaffold

            Returns
            -------
            Scaffold
                the next scaffold

        """
        self._current += 1
        self._current %= self.concentration

        return self._scaffolds[self._current]




