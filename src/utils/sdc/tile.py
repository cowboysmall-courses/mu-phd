
from typing import Tuple



class Tile:

    def __init__(self, strand: str, layout: Tuple = (12, 24, 12)):
        self.strand = strand.replace(" ", "")
        self.layout = layout


    def left(self):
        return self.strand[:self.layout[0]]

    def position(self):
        return self.strand[self.layout[0]:self.layout[0] + self.layout[1]]

    def right(self):
        return self.strand[self.layout[1] + self.layout[2]:]


    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.strand == other.strand and self.layout == other.layout
        return NotImplemented
