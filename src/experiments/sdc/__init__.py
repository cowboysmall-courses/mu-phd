
import random

from dataclasses import dataclass
from typing import List


@dataclass
class Tile:
    left_instruction: int
    right_instruction: int
    left_input: str
    right_input: str
    position: int
    value: int = 0

    def __eq__(self, other):
        if isinstance(other, Tile):
            return (self.left_instruction, self.right_instruction, self.left_input, self.right_input, self.position, self.value) == \
                (other.left_instruction, other.right_instruction, other.left_input, other.right_input, other.position, other.value)

        return NotImplemented


class Scaffold:

    def __init__(self, anchor):
        self._tiles: List[Tile | None] = [anchor, None, None, None]

    def __eq__(self, other):
        if isinstance(other, Scaffold):
            return self._tiles == other._tiles

        return NotImplemented


    def get_tile(self, index: int) -> Tile | None:
        """

            gets the tile at index within the scaffold

            Parameters
            ----------
            index: int
                the position within the scaffold

            Returns
            -------
            Tile | None
                the tile at the position within the scaffold, or None if no tile at that position

        """
        return self._tiles[index]

    def get_tiles(self) -> List[Tile | None]:
        """

            gets the tiles within the scaffold

            Returns
            -------
            List[Tile | None]
                the list of tiles within the scaffold

        """
        return self._tiles

    def place_tile(self, tile: Tile) -> None:
        """

            places the tile within the scaffold

            Parameters
            ----------
            tile: Tile
                the tile to replace the existing tile with

        """
        self._tiles[tile.position] = tile

    def replace_tile(self, tile: Tile) -> Tile | None:
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
        current = self._tiles[tile.position]
        self._tiles[tile.position] = tile
        return current


    def is_free(self, index: int) -> bool:
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
        return self._tiles[index] is None

    def is_taken(self, index: int) -> bool:
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
        return self._tiles[index] is not None

    def is_eligible(self, tile: Tile) -> bool:
        """

            checks eligibility of the tile to be placed in the scaffold at it's position

            Parameters
            ----------
            tile: Tile
                the tile in question

            Returns
            -------
            bool
                whether the tile is eligible to be placed within the scaffold

        """
        return (self.__has_left(tile.position) and self.__check_left(tile)) \
            or (self.__has_right(tile.position) and self.__check_right(tile))

    def is_replaceable(self, tile: Tile) -> bool:
        """

            checks if the existing tile can be replaced

            Parameters
            ----------
            tile: Tile
                the tile in question

            Returns
            -------
            bool
                whether the tile can replace the existing tile within the scaffold

        """
        threshold = 0.125

        if self.__has_left(tile.position) and self.__check_left(tile):
            threshold -= 0.0125

        if self.__has_right(tile.position) and self.__check_right(tile):
            threshold -= 0.0125

        # return random.uniform(0, 1) > threshold
        return random.random() > threshold



    def __has_left(self, index) -> bool:
        """

            checks if there is a tile positioned to the left of the current index

            Parameters
            ----------
            index: int
                the position within the scaffold

            Returns
            -------
            bool
                whether there is a tile to the left of the position within the scaffold

        """
        return 0 < index and self._tiles[index - 1]


    def __has_right(self, index) -> bool:
        """

            checks if there is a tile positioned to the right of the current index

            Parameters
            ----------
            index: int
                the position within the scaffold

            Returns
            -------
            bool
                whether there is a tile to the right of the position within the scaffold

        """
        return index < 3 and self._tiles[index + 1]


    def __check_left(self, tile) -> bool:
        """

            checks if the existing tile does not match with the tile to it's left,
            and the new tile matches with the tile to it's left

            Parameters
            ----------
            tile: Tile
                the tile in question

            Returns
            -------
            bool
                whether the tile is a better fit within the scaffold

        """
        return (self._tiles[tile.position - 1].right_instruction != self._tiles[tile.position].left_instruction) \
            and (self._tiles[tile.position - 1].right_instruction == tile.left_instruction)


    def __check_right(self, tile) -> bool:
        """

            checks if the existing tile does not match with the tile to it's right,
            and the new tile matches with the tile to it's right

            Parameters
            ----------
            tile: Tile
                the tile in question

            Returns
            -------
            bool
                whether the tile is a better fit within the scaffold

        """
        return (self._tiles[tile.position].right_instruction != self._tiles[tile.position + 1].left_instruction) \
            and (tile.right_instruction != self._tiles[tile.position + 1].left_instruction)
