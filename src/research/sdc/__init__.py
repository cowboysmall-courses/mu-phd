
from dataclasses import dataclass

from typing import List


FMAP = {"A": "00", "C": "01", "G": "10", "T": "11"}
RMAP = {"00": "A", "01": "C", "10": "G", "11": "T"}


@dataclass
class Tile:
    left_instruction: int
    right_instruction: int
    left_input: str
    right_input: str
    value: int = 0


def print_tiles(tiles: List[Tile]) -> None:
    print(f"\t{"\n\t".join(str(tile) for tile in tiles)}")
    print("\n")
