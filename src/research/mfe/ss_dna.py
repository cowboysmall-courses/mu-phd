
import Levenshtein


DNA_01 = "GCCGCGGGCCGAAAAAACCCCCCCGGCCCGCGGC"

DNA_02 = "GCAAAAATGACCTCTTATCAAAAG\
            GAGCAATTAAAGGTACTCTCTAAT\
            CCTGACCTGTTGGAGTTTGCTTCC"


MIN_LEN = 4

MIN_GAP = 3
MAX_GAP = 8


def main() -> None:
    print("\n")
    print("\tDNA: Something\n")
    print("\n")

    # 1 - window size ranges from (minimum length) to (total length - minimum gap length) / 2

    # 2 - window slides from start to end
    # 2 - gap ranges from minimum to maximum

    # 3 - store strings + positions

    find_candidates(DNA_01)






def find_candidates(dna_string):
    LEN = len(dna_string)
    MAX_LEN = (LEN - MAX_GAP) // 2

    print(LEN)

    strings = []

    for l in range(MIN_LEN, MAX_LEN + 1):
        print(f"dna_string length: {l}")
        for g in range(MIN_GAP, MAX_GAP + 1):
            print(f"gap length: {g}")
            for i in range(MAX_LEN + 1):
                print(f"starter dna_string[{i} : {i + l}] -> {dna_string[i : i + l]}")
                for j in range(i + l + g, LEN + 1):
                    if j + l < LEN:
                        print(f"dna_string[{j} : {j + l}] -> {dna_string[j : j + l]}")



