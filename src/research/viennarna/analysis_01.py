
import RNA


TRANSLATOR = str.maketrans("U", "T")

def main() -> None:
    print("\n")
    print("\tViennaRNA Tutorial - Free Energy")
    print("\n")

    RNA.params_load_DNA_Mathews2004()

    # seq = "GAGUAGUGGAACCAGGCUAUGUUUGUGACUCGCAGACUAACA"
    seq = "GAGTAGTGGAACCAGGCTATGTTTGTGACTCGCAGACTAACA"

    fc  = RNA.fold_compound(seq)
    (ss, mfe) = fc.mfe()

    print(f"{seq}\n{ss} ({mfe:6.2f})")
