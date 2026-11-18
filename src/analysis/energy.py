
import matplotlib.pyplot as plt

from typing import List, Dict

from utils.dna import complement
from sdc.gibbs import gibbs_free_energy


def read_dna_from_file(path: str):
    lines = []

    with open(path, "r") as file:
        for line in file:
            lines.append(line.strip())

    return "".join(lines)


def plot_results(energy: List[float], file_name: str = "energy", title: str = "title") -> None:
    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))
    plt.title(title)
    plt.grid(True)
    plt.xlabel("Position")
    plt.ylabel("Gibbs Free Energy")
    plt.plot(energy, label = "Energy Landscape")
    plt.legend()
    plt.savefig(f"./output/analysis/dna/{file_name}.png")
    plt.close()


def main() -> None:
    size = 24
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    slen = len(sdna)
    srem = slen % size

    t_st = 58

    print(f"nucleotide count: {slen}")
    print(f"   position size: {size}")
    print(f"       positions: {slen // size}")
    print(f"       remainder: {slen % size}")


    for i in range(0, srem + 1):
        snrg = []
        for j in range(i, slen, size - (srem - i)):
            base = sdna[j:j + size]
            comp = complement(base)
            snrg.append(gibbs_free_energy(base, comp, 273.15 + t_st))
        plot_results(snrg, f"m13_7249_{i}_{t_st}")



