
from utils.dna import complement, self_complementary


def test_complement():
    assert complement("ATGCAT") == "TACGTA"
    assert complement("CGTTGA") == "GCAACT"


def test_non_complement():
    assert complement("ATGCAT") != "ATGCAT"
    assert complement("CGTTGA") != "CGTTGA"


def test_self_complementary():
    assert self_complementary("ATGCAT")


def test_non_self_complementary():
    assert not self_complementary("CGTTGA")
