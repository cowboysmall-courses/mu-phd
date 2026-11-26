

from nupack import Model, structure_energy, pfunc, mfe

from typing import List, Tuple


def free_energy(S1: str, S2: str, T: float) -> float:
    model = Model(material = "dna", kelvin = T)
    strct = "+".join(["("*len(S1), ")"*len(S2)])
    return structure_energy(strands = [S1, S2], structure = strct, model = model)

def minimum_free_energy(strands: List[str], T: float) -> float:
    model = Model(material = "dna", kelvin = T)
    return mfe(strands, model)[0].energy

def partition_function(strands: List[str], T: float) -> float:
    model = Model(material = "dna", kelvin = T)
    return pfunc(strands = strands, model = model)[0]

def ensemble_free_energy(strands: List[str], T: float) -> float:
    model = Model(material = "dna", kelvin = T)
    return pfunc(strands = strands, model = model)[1]
