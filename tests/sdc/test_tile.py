
from sdc.tile import Tile


def test_equality():
    a = Tile(1, "GCTGAGAAGAGG")
    b = Tile(1, "GCTGAGAAGAGG")
    c = Tile(1, "GCTGAGAAGAGG", layout = (4, 4, 4))
    d = Tile(1, "AACAGGGATGTG", layout = (0, 8, 4))
    e = Tile(1, "AACAGGGATGTG", layout = (4, 8, 0))

    assert a == b
    assert a != c
    assert a != d
    assert a != e


def test_anchor():
    tile = Tile(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))
    assert tile.right() == "GCTGAGAAGAGG"
    assert tile.right_c() == "CGACTCTTCTCC"


def test_left():
    tile = Tile(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.left() == "CCTCTTCTCAGC"
    assert tile.left_c() == "GGAGAAGAGTCG"


def test_middle():
    tile = Tile(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.middle() == "AGCGTCCAATACTGCGGAATCGTC"
    assert tile.middle_c() == "TCGCAGGTTATGACGCCTTAGCAG"


def test_right():
    tile = Tile(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.right() == "GGTCAGGATGAG"
    assert tile.right_c() == "CCAGTCCTACTC"
