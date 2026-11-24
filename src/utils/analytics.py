

from nupack import Complex, Model, Strand, complex_analysis


def free_energy_of_binding(sequence1: str, sequence2: str, T: float) -> float:
    strand1  = Strand(sequence1, name = "Strand 1")
    strand2  = Strand(sequence2, name = "Strand 2")

    complex1 = Complex(strands = [strand1])
    complex2 = Complex(strands = [strand2])
    complex3 = Complex(strands = [strand1, strand2])

    model    = Model(material = "dna", kelvin = T)

    results  = complex_analysis([complex1, complex2, complex3], model = model, compute = ["pfunc", "mfe", "pairs"])

    return results[complex3].free_energy - (results[complex1].free_energy + results[complex2].free_energy)


def partition_function(sequence: str, T: float) -> float:
    return 0

