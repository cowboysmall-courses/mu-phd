
from utils.analytics import free_energy
from utils.dna import reverse_complement, read_dna_from_file
from analysis import plot_results



def main() -> None:
    size = 24
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    slen = len(sdna)

    t_st = 65

    print("\n")
    print("\tAnalysis - Free Energy - Raw")
    print("\n")

    print()
    print(f"\t\tNucleotide Count: {slen}")
    print(f"\t\t   Position Size: {size}")
    print("\n")

    sdna += sdna[:size]

    for i in range(0, size):
        snrg = []
        for j in range(i, slen, size):
            base = sdna[j:j + size]
            if len(base) == size:
                comp = reverse_complement(base)
                snrg.append(free_energy(base, comp, 273.15 + t_st))

        print(f"\tposition {i:>2} completed...", end = "\r")

        plot_results(snrg, "raw", f"m13_7249_{i:02d}_{t_st}", title = "Free Energy - Raw")

    print("\t  all positions completed.   ")
    print("\n")
