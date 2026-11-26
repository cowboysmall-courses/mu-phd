
from nupack import Model, structure_energy


TRANSLATOR = str.maketrans("ATGC", "TACG")

def main() -> None:
    print("\n")
    print("\tNUPACK Tutorial - Complex Analysis")
    print("\n")

    S     = "GGACTGACG"
    T     = S.translate(TRANSLATOR)[::-1]
    STR_D = f"{S}+{T}"

    STR_S = "("*len(S)
    STR_T = ")"*len(T)
    STR_C = f"{STR_S}+{STR_T}"

    model = Model(material = "dna", celsius = 37)
    STR_E = structure_energy(strands = [S, T], structure = STR_C, model = model)

    print(f"{STR_D}\n{STR_C}\n\nEnergy: {STR_E}")
    print()
