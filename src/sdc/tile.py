
from utils.dna import complement

from typing import Tuple


class Tile:

    def __init__(self, layer: int, strand: str, layout: Tuple = (12, 24, 12), concentration: int = 100000):
        self.layer  = layer
        self.strand = strand
        self.layout = layout
        self.concentration = concentration

        strand = strand.replace(" ", "")

        self._l = strand[:layout[0]]
        self._m = strand[layout[0]:layout[0] + layout[1]]
        self._r = strand[layout[0] + layout[1]:]

        self._l_c = complement(self._l)
        self._m_c = complement(self._m)
        self._r_c = complement(self._r)



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



    def left(self) -> str:
        """

            get the left compute domain

            Returns
            -------
            str
                the left compute domain

        """
        return self._l

    def left_c(self) -> str:
        """

            get the complement of the left compute domain

            Returns
            -------
            str
                the complement of the left compute domain

        """
        return self._l_c

    def middle(self) -> str:
        """

            get the middle domain

            Returns
            -------
            str
                the middle domain

        """
        return self._m

    def middle_c(self) -> str:
        """

            get the complement of the middle domain

            Returns
            -------
            str
                the complement of the middle domain

        """
        return self._m_c

    def right(self) -> str:
        """

            get the right compute domain

            Returns
            -------
            str
                the right compute domain

        """
        return self._r

    def right_c(self) -> str:
        """

            get the right compute domain

            Returns
            -------
            str
                the right compute domain

        """
        return self._r_c



    def __repr__(self):
        return f"{self._l}-{self._m}-{self._r}"

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented
        return (self.layer, self.strand, self.layout, self.concentration) == (other.layer, other.strand, other.layout, other.concentration)

    def __hash__(self):
        return hash((self.layer, self.strand, self.layout, self.concentration))
