
import random

import matplotlib.pyplot as plt

from typing import List, Dict

from experiments import Simulation
from experiments.sdc import Scaffold, Tile


class SDCBindReplaceSimulation(Simulation):

    def __init__(self, scaffolds: int, anchor: Tile, tiles: List[Tile], solution: List[Tile]):
        self._scaffolds = [Scaffold(len(solution)) for _ in range(scaffolds)]
        self._anchor = anchor
        self._tiles = tiles
        self._solution = solution


    def pre_run(self, data: Dict) -> None:
        data["TOTALS"] = []
        data["STATS"]  = {}


    def pre_simulate(self, iteration: int, data: Dict) -> None:
        for scaffold in self._scaffolds:
            scaffold.initialize(self._anchor)
        data["STATS"][iteration] = []
        data["SOLVED"] = set()


    def post_step(self, iteration: int, timestep: int, data: Dict) -> None:
        data["STATS"][iteration].append(len(data["SOLVED"]))


    def post_simulate(self, iteration: int, data: Dict) -> None:
        data["TOTALS"].append(len(data["SOLVED"]))
        data.pop("SOLVED")


    def step(self, iteration: int, timestep: int, data: Dict) -> None:
        for index, scaffold in enumerate(self._scaffolds):
            if index not in data["SOLVED"]:
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
                    data["SOLVED"].add(index)


def print_results(iters: int, count: int, totals: List[int]) -> None:
    print(f"\tResults after {iters} iterations")
    print()
    for i in range(iters):
        print_result(i, count, totals[i])
    print("\n")


def print_result(iteration: int, count: int, total: int) -> None:
    print(f"\t Iteration: {iteration + 1}")
    print(f"\t     Total: {total}")
    print(f"\tProportion: {(total / count) * 100:.2f}%")
    print()


def plot_results(iters: int, total: int, timesteps: int, stats: List[List[int]], field: str, group: str, name: str) -> None:
    plt.subplots(figsize = (12, 5))
    plt.title("Time Evolution of Computation")
    plt.grid(True)
    plt.xlabel("Timestep")
    plt.ylabel("% Remaining")

    for i in range(iters):
        y = [((total - count) / total) * 100 for count in stats[i]]
        x = [timestep for timestep in range(timesteps)]
        plt.plot(x, y, label = f"experiment {i + 1}")

    plt.legend()
    plt.savefig(f"./output/experiments/{field}/{group}/{name}/experiment.png")
    plt.close()


