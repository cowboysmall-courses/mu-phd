
from utils.dna import complement, read_dna_from_file
from sdc.gibbs import gibbs_free_energy
from analysis import plot_results



def main() -> None:
    size = 24
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    slen = len(sdna)

    t_st = 58

    print(f"nucleotide count: {slen}")
    print(f"   position size: {size}")
    print(f"       positions: {slen // size}")

    for i in range(0, size):
        snrg = []
        for j in range(i, slen, size):
            base = sdna[j:j + size]
            if len(base) == size:
                comp = complement(base)
                snrg.append(gibbs_free_energy(base, comp, 273.15 + t_st))
        plot_results(snrg, "raw", f"m13_7249_{i:02d}_{t_st}")
