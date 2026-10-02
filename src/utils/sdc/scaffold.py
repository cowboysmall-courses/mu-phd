
from typing import Dict



class Scaffold:

    def __init__(self, strand: str, position_size: int = 24):
        self.strand = strand.replace(" ", "")
        self.position_size = position_size
        self.positions: Dict[str, int] = {self.strand[i:i + position_size]: i // position_size for i in range(0, len(self.strand), position_size)}


    def get_positions(self):
        return self.positions
