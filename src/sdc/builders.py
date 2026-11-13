
from sdc.scaffold import Scaffold
from sdc.tile import Tile


from typing import Dict, List, Tuple



class ScaffoldBuilder:

    def __init__(self, strand: str, position_size: int = 24, concentration: int = 1):
        self.strand = strand
        self.position_size = position_size
        self.concentration = concentration



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



    def build(self) -> Scaffold:
        """

            retrieves the next scaffold

            Returns
            -------
            Scaffold
                the next scaffold

        """
        strand = self.strand.replace(" ", "")[::-1]
        positions = [strand[i:i + self.position_size] for i in range(0, len(strand), self.position_size)]

        return Scaffold(positions, self.concentration)



    def __repr__(self):
        return self.strand

    def __eq__(self, other):
        if not isinstance(other, ScaffoldBuilder):
            return NotImplemented
        return (self.strand, self.position_size, self.concentration) == (other.strand, other.position_size, other.concentration)

    def __hash__(self):
        return hash((self.strand, self.position_size, self.concentration))



class TileBuilder:

    def __init__(self, layer: int, strand: str, layout: Tuple = (12, 24, 12), concentration: int = 1):
        self.layer  = layer
        self.strand = strand
        self.layout = layout
        self.concentration = concentration



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



    def build(self) -> Tile:
        """

            retrieves the next tile

            Returns
            -------
            Scaffold
                the next tile

        """
        strand = self.strand.replace(" ", "")
        left   = strand[:self.layout[0]]
        middle = strand[self.layout[0]:self.layout[0] + self.layout[1]]
        right  = strand[self.layout[0] + self.layout[1]:]

        return Tile(self.layer, left, middle, right, self.concentration)



    def __repr__(self):
        return self.strand

    def __eq__(self, other):
        if not isinstance(other, TileBuilder):
            return NotImplemented
        return (self.layer, self.strand, self.layout, self.concentration) == (other.layer, other.strand, other.layout, other.concentration)

    def __hash__(self):
        return hash((self.layer, self.strand, self.layout, self.concentration))



# class TileSetBuilder:

#     def __init__(self, scaffoldbuilder: ScaffoldBuilder, tilebuilders: List[List[TileBuilder]]):
#         self.scaffoldbuilder = scaffoldbuilder
#         self.tilebuilders = tilebuilders


#     def build(self) -> Tuple[ScaffoldBuilder, List[List[TileBuilder]]]:
#         return self.scaffoldbuilder, self.tilebuilders


#     def __repr__(self):
#         return f"{self.scaffoldbuilder}\n\n{"\n".join(["\n".join([f"{builder}" for builder in layer]) for layer in self.tilebuilders])}"

#     def __eq__(self, other):
#         if not isinstance(other, TileSetBuilder):
#             return NotImplemented
#         return (self.tilebuilders) == (other.tilebuilders)

#     def __hash__(self):
#         return hash((self.tilebuilders))

