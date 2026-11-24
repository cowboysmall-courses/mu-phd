
from nupack import Model, Strand, Complex, complex_analysis


def main() -> None:
    seq = "GGCTAGCAAAAGCTAGCC"

    model = Model(material = "dna", celsius = 37)

    a  = Strand(seq, name = "a")
    cx = Complex([a], name = "a-alone")

    result = complex_analysis([cx], model = model, compute = ["pfunc", "mfe", "pairs"])
    r = result[cx]

    print(f"{r.mfe[0].structure}: {r.mfe[0].energy:.2f} (kcal/mol)")
    print(f"ensemble free energy: {r.free_energy:.2f} (kcal/mol)")
