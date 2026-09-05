
import sys
import random

import matplotlib.pyplot as plt

from typing import List

from experiments.sdc import Scaffold, Tile
from experiments import Simulation


SCAFFOLDS = [Scaffold(4) for _ in range(5000)]

ANCHOR = Tile(0, 1, "1", "1", 0, 1)

TILES = [
    Tile(1, 1, "1", "1", 1, 1),
    Tile(0, 0, "0", "0", 1, 0),
    Tile(1, 1, "1", "1", 2, 1),
    Tile(0, 0, "0", "0", 2, 0),
    Tile(1, 1, "1", "1", 3, 1),
    Tile(0, 0, "0", "0", 3, 0)
]

SOLUTION = [
    Tile(0, 1, "1", "1", 0, 1),
    Tile(1, 1, "1", "1", 1, 1),
    Tile(1, 1, "1", "1", 2, 1),
    Tile(1, 1, "1", "1", 3, 1)
]


class SDCBitcopySimulation(Simulation):

    def __init__(self, scaffolds: List[Scaffold], anchor: Tile, tiles: List[Tile], solution: List[Tile], duration: int, data: dict):
        super().__init__(data)
        self._scaffolds = scaffolds
        self._anchor = anchor
        self._tiles = tiles
        self._solution = solution
        self._duration = duration


    def pre(self, iteration: int, data: dict) -> None:
        for scaffold in self._scaffolds:
            scaffold.initialize(self._anchor)


    def simulate(self, iteration: int, data: dict) -> None:

        # Step 1: run the simulation
        solved = set()
        data["STATS"][iteration] = []

        for timestep in range(self._duration):
            for index, scaffold in enumerate(self._scaffolds):
                if index not in solved:
                    tile = random.choice(self._tiles)

                    # if the position on the scaffold is vacant - place tile in position
                    if scaffold.is_free(tile.position):
                        scaffold.place_tile(tile)

                    # else if the position is taken, and the current tile has less or equal
                    # mismatches than the existing tile - replace the existing tile
                    elif scaffold.count_mismatches(tile) <= scaffold.count_mismatches(scaffold.get_tile(tile.position)):
                        scaffold.replace_tile(tile)
                        # consider introducing a stochastic quality to replacement - for example:
                        # if random.random() > 0.5:
                        #     scaffold.replace_tile(tile)

                    # if scaffold has solved the computation, add scaffold to solved set
                    if scaffold.get_tiles() == self._solution:
                        solved.add(index)

            data["STATS"][iteration].append(len(solved))

        # Step 2: persist the results for the current iteration
        data["TOTALS"].append(len(solved))


def main() -> None:
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    sdc   = SDCBitcopySimulation(SCAFFOLDS, ANCHOR, TILES, SOLUTION, 250, {"TOTALS": [], "STATS": {}})
    data  = sdc.run(iters)

    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer - Bind / Replace: Bitcopy")
    print("\n")

    print(f"\tResults after {iters} iterations")
    print()

    for i in range(iters):
        count = data["TOTALS"][i]
        print(f"\t Iteration: {i + 1}")
        print(f"\t     Count: {count}")
        print(f"\tProportion: {(count / len(SCAFFOLDS)) * 100:.2f}%")
        print()

    print("\n")

    plt.title("SDC - Time Evolution of Bitcopy Computation")
    plt.grid(True)
    plt.xlabel("Timestep")
    plt.ylabel("Solved")

    for i in range(iters):
        y = data["STATS"][i]
        x = [x for x in range(len(y))]
        plt.plot(x, y, label = f"experiment {i + 1}")

    plt.legend()
    plt.savefig("./output/experiments/sdc/bind_replace/experiment_bitcopy.png")
    plt.close()
