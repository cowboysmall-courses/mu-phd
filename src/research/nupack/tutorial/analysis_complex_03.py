
from nupack import Complex, Model, Strand, complex_analysis


TRANSLATOR = str.maketrans("ATGC", "TACG")

def main() -> None:
    print("\n")
    print("\tNUPACK Tutorial - Complex Analysis")
    print("\n")

    S = "GGACTGACG"
    T = S.translate(TRANSLATOR)[::-1]
    # T = "CCTGGCTGC"[::-1]

    A  = Strand(S, name = "Strand A")
    B  = Strand(T, name = "Strand B")

    complex1 = Complex(strands = [A, B])
    complex2 = Complex(strands = [A])
    complex3 = Complex(strands = [B])
    model1   = Model(material = "dna", celsius = 37)

    results  = complex_analysis([complex1, complex2, complex3], model = model1, compute = ["pfunc", "mfe", "pairs"])

    print(f"dG: {(results[complex1].free_energy - (results[complex2].free_energy + results[complex3].free_energy)):.2f} (kcal/mol)")
    print()

    print(results)
    print()
