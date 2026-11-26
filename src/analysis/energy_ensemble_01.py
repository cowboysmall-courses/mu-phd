
from utils.analytics import ensemble_free_energy
from utils.dna import read_dna_from_file
from analysis import plot_results



def main() -> None:
    size = 624
    sdna = read_dna_from_file("./data/dna/m13_7249.txt")
    slen = len(sdna)

    t_st = 65

    print()
    print(f"nucleotide count: {slen}")
    print(f"   position size: {size}")
    print()

    snrg = []

    for i in range(1000):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    print("1000 Positions...")

    for i in range(1000, 2000):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    print("2000 Positions...")

    for i in range(2000, 3000):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    print("3000 Positions...")

    for i in range(3000, 4000):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    print("4000 Positions...")

    for i in range(4000, 5000):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    print("5000 Positions...")

    for i in range(5000, 6000):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    print("6000 Positions...")

    for i in range(6000, slen - size):
        base = sdna[i:i + size]
        snrg.append(ensemble_free_energy([base], 273.15 + t_st))

    plot_results(snrg, "ensemble", f"m13_7249_{t_st}")
