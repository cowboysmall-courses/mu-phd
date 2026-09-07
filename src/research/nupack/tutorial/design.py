from nupack import *


def main() -> None:
    print("\n")
    print("\tNUPACK Tutorial - Design a Tube")
    print("\n")

    a   = Domain('A4',   name = 'Domain a')
    b   = Domain('N10',  name = 'Domain b')
    c   = Domain('R5N5', name = 'Domain c')

    A   = TargetStrand([a, a, b], name = 'Strand A')
    B   = TargetStrand([~b, ~c],  name = 'Strand B')
    C   = TargetStrand([c],       name = 'Strand C')

    C1  = TargetComplex([A, B, C], '.8(10+)10(10+)10', name = 'Complex C1')
    C2  = TargetComplex([B, C],    '.10(10+)10',       name = 'Complex C2')

    tt1 = TargetTube(on_targets = {C1: 1e-8, C2: 1e-8}, off_targets = SetSpec(max_size = 3), name = 'TargetTube 1')

    model1  = Model(material = 'rna', celsius = 37)
    my_des  = tube_design(tubes = [tt1], hard_constraints = [], soft_constraints = [], defect_weights = None, options = None, model = model1)
    results = my_des.run(trials = 3)

    print(results)
    print("\n")
