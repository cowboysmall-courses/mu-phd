
from nupack import Complex, Model, Strand, complex_analysis

from utils.analytics import free_energy


TRANSLATOR = str.maketrans("ATGC", "TACG")

def main() -> None:
    print("\n")
    print("\tNUPACK Tutorial - Complex Analysis")
    print("\n")

    S = "CGTTGA"
    T = S.translate(TRANSLATOR)[::-1]

    A  = Strand(S, name = "Strand A")
    B  = Strand(T, name = "Strand B")

    complex1 = Complex(strands = [A, B])
    complex2 = Complex(strands = [A])
    complex3 = Complex(strands = [B])
    model1   = Model(material = "dna", kelvin = 310.15)

    results  = complex_analysis([complex1, complex2, complex3], model = model1, compute = ["pfunc", "mfe", "pairs"])

    print(f"dG: {(results[complex1].free_energy - (results[complex2].free_energy + results[complex3].free_energy)):.3f} (kcal/mol)")
    print(f"dG: {(free_energy(S, T, 310.15)):.3f} (kcal/mol)")
    print()

    print(results)
    print()
