
import sys

from experiments.sdc.bind_replace import SDCBindReplaceSimulation, print_results, plot_results
from experiments.sdc.bind_replace.hamilton import ANCHOR_01, TILES, SOLUTION_01


SCAFFOLDS = 5000
TIMESTEPS = 10000

def main() -> None:
    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer (Bind / Replace) - Hamiltonian Path")
    print("\n")

    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    data  = SDCBindReplaceSimulation(SCAFFOLDS, ANCHOR_01, TILES, SOLUTION_01).run(iters, TIMESTEPS)

    print_results(iters, SCAFFOLDS, data)
    plot_results(iters, SCAFFOLDS, TIMESTEPS, data, "SDC (Bind / Replace) - Time Evolution of Hamiltonian Path Computation", "sdc", "bind_replace", "hamilton")
