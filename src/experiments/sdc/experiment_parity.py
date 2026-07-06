
from experiments.sdc import Scaffold, Tile

from simulations import Simulation

import random


T_COUNT = 1000000
S_COUNT = 10000

SOLUTION = [
    Tile(0, 1, "10", "10", 0, 1),
    Tile(1, 0, "10", "01", 1, 0),
    Tile(0, 1, "01", "00", 2, 1),
    Tile(1, 1, "00", "--", 3, 1)
]


class SDCParitySimulation(Simulation):

    def step(self, iteration: int, data: dict) -> None:

        # Step 1: create a fixed number of tiles of each type, for each scaffold position
        tiles = []
        for _ in range(data["T_COUNT"]):
            tiles.append(Tile(0, 1, "10", "01", 1, 1))
            tiles.append(Tile(1, 0, "10", "01", 1, 0))
            tiles.append(Tile(0, 1, "01", "00", 2, 1))
            tiles.append(Tile(1, 0, "01", "00", 2, 0))
            tiles.append(Tile(1, 1, "00", "--", 3, 1))
            tiles.append(Tile(0, 0, "00", "--", 3, 0))

        # Step 2: create a fixed number of scaffolds for the operation, with anchor tiles
        scaffolds = []
        for _ in range(data["S_COUNT"]):
            scaffolds.append(Scaffold(Tile(0, 1, "10", "10", 0, 1)))

        # Step 3: run the simulation for each scaffold for each position
        random.shuffle(tiles)
        for _ in range(100):
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

        count = 0
        for scaffold in scaffolds:
            count += scaffold.get_tiles() != data["SOLUTION"]

        data["COUNTS"].append(count)



def main() -> None:
    iterations = 10

    sdc  = SDCParitySimulation({"T_COUNT": T_COUNT, "S_COUNT": S_COUNT, "SOLUTION": SOLUTION, "COUNTS": []})
    data = sdc.run(iterations)

    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer: Parity")
    print("\n")


    print(f"\tResults after {iterations} iterations")
    print()

    for i in range(iterations):
        count = data["COUNTS"][i]
        print(f"\t Iteration: {i + 1}")
        print(f"\t     Count: {count}")
        print(f"\tProportion: {(count / S_COUNT) * 100:.2f}%")
        print()

    print("\n")
