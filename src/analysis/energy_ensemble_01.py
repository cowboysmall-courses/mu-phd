
from utils.analytics import ensemble_free_energy
from utils.dna import reverse_complement, read_dna_from_file
from analysis import plot_results



def main() -> None:
    size = 624
    # sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    sdna = read_dna_from_file("./data/dna/m13_7249_domains.txt").replace(" ", "")
    slen = len(sdna)

    t_st = 65

    print("\n")
    print("\tAnalysis - Free Energy - Ensemble [5'-3']")
    print("\n")

    print()
    print(f"\t\tNucleotide Count: {slen}")
    print(f"\t\t   Position Size: {size}")
    print("\n")

    sdna += sdna[:size]

    snrg1 = []
    snrg2 = []
    for i in range(slen):
        base1 = sdna[i:i + size]
        base2 = reverse_complement(base1)
        snrg1.append(ensemble_free_energy([base1], 273.15 + t_st))
        snrg2.append(ensemble_free_energy([base2], 273.15 + t_st))
        if (i + 1) % 10 == 0:
            print(f"\t{i + 1:>5} positions calculated...", end = "\r")

    plot_results(snrg1, snrg2, "Energy", "Energy (RC)", "ensemble", f"m13_7249_[5-3]_{t_st}", title = "Free Energy - Ensemble [5'-3']")

    print("\t  all positions calculated.   ")
    print("\n")
