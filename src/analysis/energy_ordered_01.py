
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
    print(f"\tNucleotide Count: {slen}")
    print(f"\t   Position Size: {size}")
    print()

    snrg = []

    for i in range(0, size):

        tnrg = []

        for j in range(i, slen, size):
            base = sdna[j:j + size]
            if len(base) == size:
                comp = reverse_complement(base)
                tnrg.append((free_energy(base, comp, 273.15 + t_st), j, j + size, base))

        tnrg.sort(key = lambda x: x[0])
        data = [x[0] for x in tnrg]

        plot_results(data, "ordered/offset", f"m13_7249_{i:02d}_{t_st}", f"Free Energy - Plot - Offset {i}")
        hist_results(data, "ordered/offset", f"m13_7249_{i:02d}_{t_st}", f"Free Energy - Hist - Offset {i}")
        dist_results(data, "ordered/offset", f"m13_7249_{i:02d}_{t_st}", f"Free Energy - Dist - Offset {i}")

        snrg.extend(tnrg)

    snrg.sort(key = lambda x: x[0])
    data = [x[0] for x in snrg]

    plot_results(data, "ordered/total", f"m13_7249_{t_st}", f"Free Energy - Plot")
    hist_results(data, "ordered/total", f"m13_7249_{t_st}", f"Free Energy - Hist")
    dist_results(data, "ordered/total", f"m13_7249_{t_st}", f"Free Energy - Dist")
