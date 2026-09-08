
import sys

from experiments.sdc.bind_replace import SDCBindReplaceSimulation, print_results, plot_results
from experiments.sdc.bind_replace.counter import *


SCAFFOLDS = 5000
TIMESTEPS = 500

def main() -> None:
    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer (Bind / Replace) - Counter - 4 Computations")
    print("\n")

    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5


    print("\tFirst Computation: 0 -> 4")
    print()
    data  = SDCBindReplaceSimulation(SCAFFOLDS, ANCHOR_01, TILES, SOLUTION_01).run(iters, TIMESTEPS)
    print_results(iters, SCAFFOLDS, data)
    plot_results(iters, SCAFFOLDS, TIMESTEPS, data, "SDC (Bind / Replace) - Time Evolution of Counter Computation: 0 -> 4", "sdc", "bind_replace", "counter", "experiment_01")


    print("\tSecond Computation: 2 -> 6")
    print()
    data  = SDCBindReplaceSimulation(SCAFFOLDS, ANCHOR_02, TILES, SOLUTION_02).run(iters, TIMESTEPS)
    print_results(iters, SCAFFOLDS, data)
    plot_results(iters, SCAFFOLDS, TIMESTEPS, data, "SDC (Bind / Replace) - Time Evolution of Counter Computation: 2 -> 6", "sdc", "bind_replace", "counter", "experiment_02")


    print("\tThird Computation: 4 -> 0")
    print()
    data  = SDCBindReplaceSimulation(SCAFFOLDS, ANCHOR_03, TILES, SOLUTION_03).run(iters, TIMESTEPS)
    print_results(iters, SCAFFOLDS, data)
    plot_results(iters, SCAFFOLDS, TIMESTEPS, data, "SDC (Bind / Replace) - Time Evolution of Counter Computation: 4 -> 0", "sdc", "bind_replace", "counter", "experiment_03")


    print("\tFourth Computation: 6 -> 2")
    print()
    data  = SDCBindReplaceSimulation(SCAFFOLDS, ANCHOR_04, TILES, SOLUTION_04).run(iters, TIMESTEPS)
    print_results(iters, SCAFFOLDS, data)
    plot_results(iters, SCAFFOLDS, TIMESTEPS, data, "SDC (Bind / Replace) - Time Evolution of Counter Computation: 6 -> 2", "sdc", "bind_replace", "counter", "experiment_04")
