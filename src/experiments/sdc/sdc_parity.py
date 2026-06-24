
from experiments.sdc import Tile

from typing import List

PMAP = {"00": 0, "01": 1, "10": 1, "11": 0}

def get_parity_tiles(bits: str) -> List[Tile]:
    chunks = [bits[i:i + 2] for i in range(0, len(bits), 2)]

    tiles  = [Tile(0, PMAP[chunks[0]], chunks[0], chunks[1], PMAP[chunks[0]])]
    for i in range(1, len(chunks) - 1):
        b1 = chunks[i]
        b2 = chunks[i + 1]
        tiles.append(Tile(tiles[-1].right_instruction, (tiles[-1].right_instruction + PMAP[b1]) % 2, b1, b2, (tiles[-1].value + PMAP[b1]) % 2))
    tiles.append(Tile(tiles[-1].right_instruction, (tiles[-1].right_instruction + PMAP[chunks[-1]]) % 2, chunks[-1], "--", (tiles[-1].value + PMAP[chunks[-1]]) % 2))

    return tiles


def main() -> None:
    print("SDC: Parity\n")

    bits  = "10100100"
    tiles = get_parity_tiles(bits)
    print(f"Parity({bits}) = {tiles[-1].value}")
    print("\n".join(str(tile) for tile in tiles))
    print()


    bits  = "00100100"
    tiles = get_parity_tiles(bits)
    print(f"Parity({bits}) = {tiles[-1].value}")
    print("\n".join(str(tile) for tile in tiles))
    print()


    bits  = "11111111"
    tiles = get_parity_tiles(bits)
    print(f"Parity({bits}) = {tiles[-1].value}")
    print("\n".join(str(tile) for tile in tiles))
    print()


    bits  = "00000000"
    tiles = get_parity_tiles(bits)
    print(f"Parity({bits}) = {tiles[-1].value}")
    print("\n".join(str(tile) for tile in tiles))
    print()
