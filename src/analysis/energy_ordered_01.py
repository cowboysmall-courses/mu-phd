
from utils.analytics import free_energy
from utils.dna import reverse_complement, read_dna_from_file
from analysis import plot_results, hist_results, dist_results



def main() -> None:
    size = 24
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    slen = len(sdna)

    t_st = 58

    print("\n")
    print("\tAnalysis - Free Energy - Ordered")
    print("\n")

    print()
    print(f"\t\tNucleotide Count: {slen}")
    print(f"\t\t   Position Size: {size}")
    print("\n")

    sdna += sdna[:size]

    snrg = []
    for i in range(size):
        tnrg = []
        for j in range(i, slen, size):
            base = sdna[j:j + size]
            tnrg.append((free_energy(base, reverse_complement(base), 273.15 + t_st), j, j + size, base))
        tnrg.sort(key = lambda x: x[0])
        data = [x[0] for x in tnrg]

        plot_results(data, "ordered/offset", f"m13_7249_{i:02d}_{t_st}", f"Free Energy - Ordered - Plot (Offset {i})")
        hist_results(data, "ordered/offset", f"m13_7249_{i:02d}_{t_st}", f"Free Energy - Ordered - Hist (Offset {i})")
        dist_results(data, "ordered/offset", f"m13_7249_{i:02d}_{t_st}", f"Free Energy - Ordered - Dist (Offset {i})")

        snrg.extend(tnrg)

    snrg.sort(key = lambda x: x[0])
    data = [x[0] for x in snrg]

    plot_results(data, "ordered/total", f"m13_7249_{t_st}", f"Free Energy - Ordered - Plot")
    hist_results(data, "ordered/total", f"m13_7249_{t_st}", f"Free Energy - Ordered - Hist")
    dist_results(data, "ordered/total", f"m13_7249_{t_st}", f"Free Energy - Ordered - Dist")
