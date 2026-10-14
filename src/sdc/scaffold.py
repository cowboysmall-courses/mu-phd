
from sdc.tile import Tile

# from utils.dna import complement

from typing import Dict, List


class Scaffold:

    def __init__(self, strand: str, position_size: int = 24):
        self.strand = strand[::-1].replace(" ", "")
        self.position_size = position_size

        self._positions: List[str] = [self.strand[i:i + position_size] for i in range(0, len(self.strand), position_size)]

        self._position_count: int = len(self._positions)
        self._position_index: Dict[str, int] = {p:i for i, p in enumerate(self._positions)}

        self._bindings: Dict[int, Tile | None] = {i:None for i in range(self._position_count)}



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



    def get_positions(self) -> List[str]:
        return self._positions

    def get_position_count(self) -> int:
        return self._position_count

    def get_position_index(self, position: str) -> int:
        return self._position_index[position]


    def get_bound_tiles(self) -> List[Tile | None]:
        return [self._bindings[i] for i in range(self._position_count)]




    # def mismatches(self, tile: Tile) -> int:
    #     position = self._position_index[tile.middle_c()]
    #     mismatches = 0
    #     # if position > 0 and self._bindings[position - 1]:
    #     #     mismatches += tile.mismatch_left(self._bindings[position - 1])
    #     return mismatches
