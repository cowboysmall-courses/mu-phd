
from sdc.tile import Tile

from typing import Dict, List


class Scaffold:

    def __init__(self, strand: str, position_size: int = 24):
        self.strand = strand
        self.position_size = position_size

        strand = strand.replace(" ", "")[::-1]

        self._positions: List[str] = [strand[i:i + position_size] for i in range(0, len(strand), position_size)]
        self._position_count: int = len(self._positions)
        self._position_index: Dict[str, int] = {p:i for i, p in enumerate(self._positions)}
        self._bindings: Dict[int, Tile | None] = {i:None for i in range(self._position_count)}



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



    def get_positions(self) -> List[str]:
        """

            get the positions on the scaffold

            Returns
            -------
            List[str]
                the positions on the scaffold

        """
        return self._positions

    def get_position_count(self) -> int:
        """

            get the number of positions on the scaffold

            Returns
            -------
            int
                the number of positions of the scaffold

        """
        return self._position_count

    def get_position_index(self, position: str) -> int:
        """

            get the index of the position on the scaffold

            Returns
            -------
            int
                the index of the position on the scaffold

        """
        return self._position_index[position]

    def get_bound_tiles(self) -> List[Tile | None]:
        """

            get a list of the bound tiles on the scaffold

            Returns
            -------
            List[Tile | None]
                a list of the bound tiles on the scaffold

        """
        return [self._bindings[i] for i in range(self._position_count)]



    def bind(self, tile: Tile) -> None:
        """

            binds the tile to the scaffold

            Parameters
            ----------
            tile: Tile
                the tile to bind to the scaffold

        """
        position = self._position_index[tile.middle_c()]
        self._bindings[position] = tile

    def unbind(self, tile: Tile) -> None:
        """

            unbinds the tile from the scaffold

            Parameters
            ----------
            tile: Tile
                the tile to unbind from the scaffold

        """
        position = self._position_index[tile.middle_c()]
        self._bindings[position] = None

    def replace(self, tile: Tile) -> Tile | None:
        """

            replaces the tile within the scaffold, returning the replaced tile

            Parameters
            ----------
            tile: Tile
                the tile to replace the existing tile with

            Returns
            -------
            Tile | None
                the tile replaced, or None if no tile was replaced

        """
        position = self._position_index[tile.middle_c()]
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
        position = self._position_index[tile.middle_c()]
        return self._bindings[position] is None

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
        position = self._position_index[tile.middle_c()]
        return self._bindings[position] is not None








    # def mismatches(self, tile: Tile) -> int:
    #     position = self._position_index[tile.middle_c()]
    #     mismatches = 0
    #     # if position > 0 and self._bindings[position - 1]:
    #     #     mismatches += tile.mismatch_left(self._bindings[position - 1])
    #     return mismatches
