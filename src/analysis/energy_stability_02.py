
from utils.analytics import ensemble_free_energy, minimum_free_energy
from utils.dna import reverse_complement, read_dna_from_file
from analysis import plot_results



def main() -> None:
    size = 624
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")[::-1]
    slen = len(sdna)

    t_st = 65

    print("\n")
    print("\tAnalysis - Free Energy - Stability (Reverse Complement)")
    print("\n")

    print()
    print(f"\t\tNucleotide Count: {slen}")
    print(f"\t\t   Position Size: {size}")
    print("\n")

    sdna += sdna[:size]

    snrg = []
    for i in range(slen):
        base = reverse_complement(sdna[i:i + size])
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)
        if (i + 1) % 10 == 0:
            print(f"\t{i + 1:>5} positions calculated...", end = "\r")

    plot_results(snrg, "stability", f"m13_7249_{t_st}_rc", title = "Free Energy - Stability (Reverse Complement)")

    print("\t  all positions calculated.   ")
    print("\n")
