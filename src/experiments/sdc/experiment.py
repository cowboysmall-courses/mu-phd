
from experiments.sdc import Scaffold, Tile

import random


T_COUNT = 1000000
S_COUNT = 10000

SOLUTION = [
    Tile(0, 1, "10", "10", 0, 1),
    Tile(1, 0, "10", "01", 1, 0),
    Tile(0, 1, "01", "00", 2, 1),
    Tile(1, 1, "00", "--", 3, 1)
]


def main() -> None:
    # Step 1: create a fixed number of tiles of each type, for each scaffold position
    tiles = []
    for _ in range(T_COUNT):
        tiles.append(Tile(0, 1, "10", "01", 1, 1))
        tiles.append(Tile(1, 0, "10", "01", 1, 0))
        tiles.append(Tile(0, 1, "01", "00", 2, 1))
        tiles.append(Tile(1, 0, "01", "00", 2, 0))
        tiles.append(Tile(1, 1, "00", "--", 3, 1))
        tiles.append(Tile(0, 0, "00", "--", 3, 0))

    # Step 2: create a fixed number of scaffolds for the operation, with anchor tiles
    scaffolds = []
    for _ in range(S_COUNT):
        scaffolds.append(Scaffold(Tile(0, 1, "10", "10", 0, 1)))

    # Step 3: run the simulation for each scaffold for each position
    random.shuffle(tiles)
    for i in range(100):
        for scaffold in scaffolds:
            tile = tiles.pop()

            # if position vacant - place tile
            if scaffold.is_free(tile.position):
                scaffold.place_tile(tile)

            # else if position taken, eligible, and replaceable - replace tile
            elif scaffold.is_eligible(tile) and scaffold.is_replaceable(tile):
                tiles.append(scaffold.replace_tile(tile))

            # else return tile to the solution
            else:
                tiles.append(tile)

    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer: Parity")
    print("\n")

    count = 0
    for scaffold in scaffolds:
        count += scaffold.tiles != SOLUTION

    print("\tSuccess")
    print()
    print(f"\t     Count: {count}")
    print(f"\tProportion: {(count / S_COUNT) * 100:.2f}%")
    print("\n")
