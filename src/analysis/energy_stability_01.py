
from utils.analytics import ensemble_free_energy, minimum_free_energy
from utils.dna import read_dna_from_file
from analysis import plot_results



def main() -> None:
    size = 624
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    slen = len(sdna)

    t_st = 65

    print("\n")
    print("\tAnalysis - Free Energy - Stability")
    print("\n")

    print()
    print(f"\tNucleotide Count: {slen}")
    print(f"\t   Position Size: {size}")
    print()

    snrg = []

    for i in range(slen - size):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_MFE - G_EFE)
        if (i + 1) % 100 == 0:
            print(f"\t\t{i + 1:>5} positions calculated ...", end = "\r")

    plot_results(snrg, "stability", f"m13_7249_{t_st}")

    print("\t\t  all positions calculated.  ")
    print("\n")
