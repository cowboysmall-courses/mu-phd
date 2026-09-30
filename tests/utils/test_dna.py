
from utils.dna import complement, is_self_complementary


def test_complement():
    assert complement("ATGCAT") == "TACGTA"
    assert complement("CGTTGA") == "GCAACT"


def test_non_complement():
    assert complement("ATGCAT") != "ATGCAT"
    assert complement("CGTTGA") != "CGTTGA"


def test_is_self_complementary():
    assert is_self_complementary("ATGCAT")


def test_is_non_self_complementary():
    assert not is_self_complementary("CGTTGA")
