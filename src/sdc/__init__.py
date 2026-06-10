
from typing import List

from dataclasses import dataclass


FMAP = {"A": "00", "C": "01", "G": "10", "T": "11"}
RMAP = {"00": "A", "01": "C", "10": "G", "11": "T"}


PMAP = {"00": 0, "01": 1, "10": 1, "11": 0}


@dataclass
class Tile:
    left_instruction: int
    right_instruction: int
    left_input: str
    right_input: str
    left_encoded: str
    right_encoded: str


def get_tiles(bits: str) -> List[Tile]:
    if len(bits) % 2 == 1:
        bits = "0" + bits

    chunks = [bits[i:i + 2] for i in range(0, len(bits), 2)]

    tiles  = [Tile(0, PMAP[chunks[0]], chunks[0], chunks[1], RMAP[chunks[0]], RMAP[chunks[1]])]
    for i in range(1, len(chunks) - 1):
        b1 = chunks[i]
        b2 = chunks[i + 1]
        tiles.append(Tile(tiles[-1].right_instruction, (tiles[-1].right_instruction + PMAP[b1]) % 2, b1, b2, RMAP[b1], RMAP[b2]))
    tiles.append(Tile(tiles[-1].right_instruction, (tiles[-1].right_instruction + PMAP[chunks[-1]]) % 2, chunks[-1], "  ", RMAP[chunks[-1]], " "))

    return tiles
