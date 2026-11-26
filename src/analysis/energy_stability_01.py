
from utils.analytics import free_energy, ensemble_free_energy, minimum_free_energy
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
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    print("1000 Positions...")

    for i in range(1000, 2000):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    print("2000 Positions...")

    for i in range(2000, 3000):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    print("3000 Positions...")

    for i in range(3000, 4000):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    print("4000 Positions...")

    for i in range(4000, 5000):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    print("5000 Positions...")

    for i in range(5000, 6000):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    print("6000 Positions...")

    for i in range(6000, slen - size):
        base = sdna[i:i + size]
        G_MFE = minimum_free_energy([base], 273.15 + t_st)
        G_EFE = ensemble_free_energy([base], 273.15 + t_st)
        snrg.append(G_EFE - G_MFE)

    plot_results(snrg, "stability", f"m13_7249_{t_st}")
