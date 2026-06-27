
from research.sdc import Tile

from typing import List

def get_add_tiles(bits1: str, bits2: str) -> List[Tile]:
    chunks = [f"{b1}{b2}" for b1, b2 in zip(reversed(bits1), reversed(bits2))]

    z = sum([int(b) for b in chunks[0]])
    tiles = [Tile(0, z // 2, chunks[0], chunks[1], z % 2)]
    for i in range(1, len(chunks) - 1):
        z = sum([int(b) for b in chunks[i]])
        tiles.append(Tile(tiles[-1].right_instruction, (tiles[-1].right_instruction + z) // 2, chunks[i], chunks[i + 1], (tiles[-1].right_instruction + z) % 2))
    z = sum([int(b) for b in chunks[-1]])
    tiles.append(Tile(tiles[-1].right_instruction, tiles[-1].right_instruction, chunks[-1], "--", (tiles[-1].right_instruction + z) % 2))

    return tiles


def main() -> None:
    print("SDC: Add\n")

    bits1 = "1010"
    bits2 = "0011"
    tiles = get_add_tiles(bits1, bits2)
    print(f"{bits1} + {bits2} = {''.join(reversed([str(tile.value) for tile in tiles]))}")
    print("\n".join(str(tile) for tile in tiles))
    print()


    bits1 = "0111"
    bits2 = "0001"
    tiles = get_add_tiles(bits1, bits2)
    print(f"{bits1} + {bits2} = {''.join(reversed([str(tile.value) for tile in tiles]))}")
    print("\n".join(str(tile) for tile in tiles))
    print()


    bits1 = "1100"
    bits2 = "0011"
    tiles = get_add_tiles(bits1, bits2)
    print(f"{bits1} + {bits2} = {''.join(reversed([str(tile.value) for tile in tiles]))}")
    print("\n".join(str(tile) for tile in tiles))
    print()


    bits1 = "1111"
    bits2 = "0001"
    tiles = get_add_tiles(bits1, bits2)
    print(f"{bits1} + {bits2} = {''.join(reversed([str(tile.value) for tile in tiles]))}")
    print("\n".join(str(tile) for tile in tiles))
    print()
