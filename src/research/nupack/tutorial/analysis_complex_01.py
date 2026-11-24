
from nupack import ComplexSet, Model, SetSpec, Strand, complex_analysis


TRANSLATOR = str.maketrans("ATGC", "TACG")

def main() -> None:
    print("\n")
    print("\tNUPACK Tutorial - Complex Analysis")
    print("\n")

    S = "CGTTGA"
    T = S.translate(TRANSLATOR)[::-1]

    A  = Strand(S, name = "Strand A")
    B  = Strand(T, name = "Strand B")

    complex1 = ComplexSet(strands = [A, B], complexes = SetSpec(max_size = 2))
    model1   = Model(material = "dna", celsius = 37)

    results  = complex_analysis(complexes = complex1, model = model1, compute = ["pfunc", "mfe", "pairs"])

    for complex in complex1.complexes:
        print(f"{complex.name:>20} dG: {results[complex].free_energy:.3f} (kcal/mol)")
    print()

    print(results)
    print()
