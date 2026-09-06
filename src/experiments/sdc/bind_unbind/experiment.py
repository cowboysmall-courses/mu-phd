import sys
import random

from experiments.sdc import Scaffold, Tile
from experiments import Simulation


T_COUNT = 1
S_COUNT = 1

class SDCBindUnbindSimulation(Simulation):

    def step(self, iteration: int, data: dict) -> None:

        # Step 1: create a fixed number of tiles of each type, for each scaffold position
        tiles = []

        # Step 2: create a fixed number of scaffolds for the operation, with anchor tiles
        scaffolds = []

        # Step 3: run the simulation for each scaffold for each position
        random.shuffle(tiles)
        for _ in range(5000):
            for scaffold in scaffolds:
                # bind / unbind
                continue

        count = 0

        data["COUNTS"].append(count)


def main() -> None:
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    sdc   = SDCBindUnbindSimulation({"T_COUNT": T_COUNT, "S_COUNT": S_COUNT, "SOLUTION": [], "COUNTS": []})
    data  = sdc.run(iters)

    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer - Bind / Unbind: Bitcopy")
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
