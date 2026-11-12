
from utils.dna import complement

from typing import Dict, List, Tuple



class Tile:

    # def __init__(self, layer: int, left: str, middle: str, right: str, bound: bool = False):
    def __init__(self, layer: int, left: str, middle: str, right: str):
        self.layer = layer
        self.left = left
        self.middle = middle
        self.right = right
        # self.bound = bound

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



    # def bind(self) -> None:
    #     """

    #         marks this tile as bound

    #     """
    #     self.bound = True

    # def unbind(self) -> None:
    #     """

    #         marks this tile as unbound

    #     """
    #     self.bound = False

    # def is_bound(self) -> bool:
    #     """

    #         is this tile bound?

    #         Returns
    #         -------
    #         bool
    #             true if the tile is bound, false otherwise

    #     """
    #     return self.bound



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




class TileManager:

    def __init__(self, layer: int, strand: str, layout: Tuple = (12, 24, 12), concentration: int = 1):
        self.layer  = layer
        self.strand = strand
        self.layout = layout
        self.concentration = concentration

        self._tiles: List[Tile] = []
        self._count: int = 0
        self._current: int = 0

        strand = strand.replace(" ", "")
        for _ in range(self.concentration):
            self._tiles.append(Tile(self.layer, strand[:layout[0]], strand[layout[0]:layout[0] + layout[1]], strand[layout[0] + layout[1]:]))



    def get_layer(self) -> int:
        """

            get the layer the tile occupies

            Returns
            -------
            int
                the layer the tile occupies

        """
        return self.layer

    def get_strand(self) -> str:
        """

            get the underlying strand of the tile

            Returns
            -------
            str
                the underlying strand of the tile

        """
        return self.strand

    def get_layout(self) -> Tuple:
        """

            get the tile layout

            Returns
            -------
            Tuple
                the tile layout

        """
        return self.layout

    def get_concentration(self) -> int:
        """

            get the initial tile concentration

            Returns
            -------
            int
                the initial tile concentration

        """
        return self.concentration



    def next(self) -> Tile:
        """

            retrieves the next tile

            Returns
            -------
            Scaffold
                the next tile

        """
        self._current += 1
        self._current %= self.concentration

        return self._tiles[self._current]



    def __repr__(self):
        return self.strand

    def __eq__(self, other):
        if not isinstance(other, TileManager):
            return NotImplemented
        return (self.layer, self.strand, self.layout, self.concentration) == (other.layer, other.strand, other.layout, other.concentration)

    def __hash__(self):
        return hash((self.layer, self.strand, self.layout, self.concentration))

