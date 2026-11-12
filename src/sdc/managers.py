
from sdc.scaffold import Scaffold


from typing import Dict, List
from abc import ABC




class Manager(ABC):

    def __init__(self):
        pass



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

            get the initial scaffold concentration

            Returns
            -------
            int
                the initial scaffold concentration

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



    def __repr__(self):
        return self.strand

    def __eq__(self, other):
        if not isinstance(other, ScaffoldManager):
            return NotImplemented
        return (self.strand, self.position_size, self.concentration) == (other.strand, other.position_size, other.concentration)

    def __hash__(self):
        return hash((self.strand, self.position_size, self.concentration))
