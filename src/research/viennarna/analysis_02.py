
import RNA


# TRANSLATOR = str.maketrans("U", "T")
TRANSLATOR = str.maketrans("ATGC", "TACG")

def main() -> None:
    print("\n")
    print("\tViennaRNA Tutorial - Free Energy")
    print("\n")

    RNA.params_load_DNA_Mathews2004()

    md = RNA.md()
    md.temperature = 37.0

    seq1 = "CGTTGA"
    seq2 = "CGTTGA"
    # seq1 = "ATTTTTGATTTATGGTCATTCTCG"
    # seq2 = "ATTTTTGATTTATGGTCATTCTCG"

    duplex = RNA.duplexfold(seq1, seq2)
    print(f"{duplex.structure} {duplex.energy:.2f} (kcal/mol)")

    fc      = RNA.fold_compound(seq1 + "&" + seq2, md)
    ss, mfe = fc.mfe_dimer()
    print(f"{ss} {mfe:.2f} (kcal/mol)")

