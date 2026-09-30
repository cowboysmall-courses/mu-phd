
COMP = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}


def complement(DNA: str) -> str:
    return "".join(COMP[N] for N in DNA)


def self_complementary(DNA: str) -> bool:
    return complement(DNA) == DNA[::-1]
