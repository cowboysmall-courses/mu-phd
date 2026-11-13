
from utils.dna import complement

from typing import Dict, List, Tuple



class Tile:

    def __init__(self, layer: int, left: str, middle: str, right: str, concentration: int = 1):
        self.layer = layer
        self.left = left
        self.middle = middle
        self.right = right
        self.concentration = concentration

        self._left_c = complement(self.left)
        self._middle_c = complement(self.middle)
        self._right_c = complement(self.right)



    def get_layer(self) -> int:
        """

            get the layer the tile occupies

            Returns
            -------
            int
                the layer the tile occupies

        """
        return self.layer

    def get_left(self) -> str:
        """

            get the left compute domain

            Returns
            -------
            str
                the left compute domain

        """
        return self.left

    def get_left_complement(self) -> str:
        """

            get the complement of the left compute domain

            Returns
            -------
            str
                the complement of the left compute domain

        """
        return self._left_c

    def get_middle(self) -> str:
        """

            get the middle domain

            Returns
            -------
            str
                the middle domain

        """
        return self.middle

    def get_middle_complement(self) -> str:
        """

            get the complement of the middle domain

            Returns
            -------
            str
                the complement of the middle domain

        """
        return self._middle_c

    def get_right(self) -> str:
        """

            get the right compute domain

            Returns
            -------
            str
                the right compute domain

        """
        return self.right

    def get_right_complement(self) -> str:
        """

            get the right compute domain

            Returns
            -------
            str
                the right compute domain

        """
        return self._right_c



    def __repr__(self):
        return f"{self.layer}: {self.left}-{self.middle}-{self.right}"

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented
        return (self.layer, self.left, self.middle, self.right) == (other.layer, other.left, other.middle, other.right)

    def __hash__(self):
        return hash((self.layer, self.left, self.middle, self.right))




class NullTile(Tile):

    def __init__(self, layer: int):
        super().__init__(layer, "", "", "")


