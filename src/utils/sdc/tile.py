
from utils.dna import complement

from typing import Tuple



class Tile:

    def __init__(self, strand: str, layout: Tuple = (12, 24, 12)):
        self.strand = strand.replace(" ", "")
        self.layout = layout

        self._left = self.strand[:layout[0]]
        self._left_c = complement(self._left)

        self._position = self.strand[layout[0]:layout[0] + layout[1]]

        self._right = self.strand[layout[1] + layout[2]:]
        self._right_c = complement(self._right)

        # self._index =

        self._left_tyle = None
        # self._left_tyle_match = 0

        self._right_tyle = None
        # self._right_tyle_match = 0


    def left(self):
        """

            get the left compute domain

            Returns
            -------
            str
                the left compute domain

        """
        return self._left

    def position(self):
        """

            get the scaffold position domain

            Returns
            -------
            str
                the scaffold position domain

        """
        return self._position

    def right(self):
        """

            get the right compute domain

            Returns
            -------
            str
                the right compute domain

        """
        return self._right



    def mismatch_left(self, tile: Tile) -> bool:
        return self._left_c != tile.right()


    def mismatch_right(self, tile: Tile) -> bool:
        return self._right_c != tile.left()




    def bind_left(self, tile: Tile):
        self._left_tyle = tile
        # self._left_tyle_match = (self._left_c == tile.right())


    def bind_right(self, tile: Tile):
        self._right_tyle = tile
        # self._right_tyle_match = (self._right_c == tile.left())




    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.strand == other.strand and self.layout == other.layout
        return NotImplemented
