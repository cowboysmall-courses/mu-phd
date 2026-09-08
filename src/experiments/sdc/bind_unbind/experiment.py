import sys
import random

from typing import List

from experiments.sdc import Scaffold, Tile
from experiments import Simulation


SCAFFOLDS = 5000

class SDCBindUnbindSimulation(Simulation):

    def __init__(self, scaffolds: int, anchor: Tile, tiles: List[Tile], solution: List[Tile]):
        self._scaffolds = [Scaffold(len(solution)) for _ in range(scaffolds)]
        self._anchor = anchor
        self._tiles = tiles
        self._solution = solution


def main() -> None:
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    data  = {"COUNTS": [random.randint(1, SCAFFOLDS) for _ in range(iters)]}

    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer - Bind / Unbind: Bitcopy")
    print("\n")


    print(f"\tResults after {iters} iterations")
    print()

    for i in range(iters):
        count = data["COUNTS"][i]
        print(f"\t Iteration: {i + 1}")
        print(f"\t     Count: {count}")
        print(f"\tProportion: {(count / SCAFFOLDS) * 100:.2f}%")
        print()

    print("\n")
