
import sys

from experiments.sdc.bind_replace import SDCBindReplaceSimulation, print_results, plot_results
from experiments.sdc.bind_replace.parity import ANCHOR, TILES, SOLUTION


SCAFFOLDS = 5000
TIMESTEPS = 100

def main() -> None:
    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer - Bind / Replace: Parity")
    print("\n")

    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    data  = SDCBindReplaceSimulation(SCAFFOLDS, ANCHOR, TILES, SOLUTION).run(iters, TIMESTEPS)

    print_results(iters, SCAFFOLDS, data["TOTALS"])
    plot_results(iters, SCAFFOLDS, TIMESTEPS, data["STATS"], "sdc", "bind_replace", "parity")
