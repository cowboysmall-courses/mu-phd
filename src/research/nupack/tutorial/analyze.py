from nupack import *


def main() -> None:
    print("\n")
    print("\tNUPACK Tutorial - Analyze a Tube")
    print("\n")

    A  = Strand('CTGATCGAT',  name = 'Strand A')
    B  = Strand('GATCGTAGTC', name = 'Strand B')
    t1 = Tube(strands = {A: 1e-8, B: 1e-9}, complexes = SetSpec(max_size = 2), name = 'Tube 1')

    model1  = Model(material = 'rna', celsius = 37)
    results = tube_analysis(tubes = [t1], model = model1)

    print(results)
    print("\n")
