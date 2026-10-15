
from utils.dna import complement

from typing import Tuple


class Tile:

    def __init__(self, strand: str, layout: Tuple = (12, 24, 12), concentration: int = 100000):
        self.strand = strand.replace(" ", "")
        self.layout = layout
        self.concentration = concentration

        self._l = self.strand[:layout[0]]
        self._l_c = complement(self._l)

        self._m = self.strand[layout[0]:layout[0] + layout[1]]
        self._m_c = complement(self._m)

        self._r = self.strand[layout[0] + layout[1]:]
        self._r_c = complement(self._r)



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
        if isinstance(other, Tile):
            return self.strand == other.strand and self.layout == other.layout
        return NotImplemented
