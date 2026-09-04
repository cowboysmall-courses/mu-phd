
import sys
import random

from experiments.sdc import Scaffold, Tile
from experiments import Simulation


T_COUNT = 100000
S_COUNT = 5000

SOLUTION = [
    Tile(0, 1, "--", "--", 0, 1),
    Tile(1, 1, "--", "--", 1, 1),
    Tile(1, 1, "--", "--", 2, 1),
    Tile(1, 1, "--", "--", 3, 1)
]


class SDCBitcopySimulation(Simulation):

    def step(self, iteration: int, data: dict) -> None:

        # Step 1: create a fixed number of tiles of each type, for each scaffold position
        tiles = []
        for _ in range(data["T_COUNT"]):
            tiles.append(Tile(1, 1, "--", "--", 1, 1))
            tiles.append(Tile(0, 0, "--", "--", 1, 0))
            tiles.append(Tile(1, 1, "--", "--", 2, 1))
            tiles.append(Tile(0, 0, "--", "--", 2, 0))
            tiles.append(Tile(1, 1, "--", "--", 3, 1))
            tiles.append(Tile(0, 0, "--", "--", 3, 0))

        # Step 2: create a fixed number of scaffolds for the operation, with anchor tiles
        scaffolds = []
        for _ in range(data["S_COUNT"]):
            scaffolds.append(Scaffold(Tile(0, 1, "--", "--", 0, 1)))

        # Step 3: run the simulation for each scaffold for each position
        random.shuffle(tiles)
        for _ in range(5000):
            for scaffold in scaffolds:
                tile = tiles.pop()

                # if position vacant - place tile
                if scaffold.is_free(tile.position):
                    scaffold.place_tile(tile)

                # else if position taken, and less mismatches - replace tile
                elif scaffold.count_mismatches(tile) <= scaffold.count_mismatches(scaffold.get_tile(tile.position)):
                    tiles.append(scaffold.replace_tile(tile))

                # else return tile to the solution
                else:
                    tiles.append(tile)

        count = 0
        for scaffold in scaffolds:
            count += scaffold.get_tiles() == data["SOLUTION"]

        data["COUNTS"].append(count)



def main() -> None:
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    sdc   = SDCBitcopySimulation({"T_COUNT": T_COUNT, "S_COUNT": S_COUNT, "SOLUTION": SOLUTION, "COUNTS": []})
    data  = sdc.run(iters)

    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer - Bind / Replace: Bitcopy")
    print("\n")


    print(f"\tResults after {iters} iterations")
    print()

    for i in range(iters):
        count = data["COUNTS"][i]
        print(f"\t Iteration: {i + 1}")
        print(f"\t     Count: {count}")
        print(f"\tProportion: {(count / S_COUNT) * 100:.2f}%")
        print()

    print("\n")
