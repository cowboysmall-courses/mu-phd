
from sdc.tile import Tile


def test_equality():
    a = Tile("GCTGAGAAGAGG")
    b = Tile("GCTGAGAAGAGG")
    c = Tile("GCTGAGAAGAGG", layout = (4, 4, 4))
    d = Tile("AACAGGGATGTG")
    e = Tile("AACAGGGATGTG", layout = (4, 4, 4))

    assert a == b
    assert a != c
    assert a != d
    assert a != e


def test_left():
    tile = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.left() == "CCTCTTCTCAGC"
    assert tile.left_c() == "GGAGAAGAGTCG"


def test_middle():
    tile = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.middle() == "AGCGTCCAATACTGCGGAATCGTC"
    assert tile.middle_c() == "TCGCAGGTTATGACGCCTTAGCAG"


def test_right():
    tile = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.right() == "GGTCAGGATGAG"
    assert tile.right_c() == "CCAGTCCTACTC"


def test_anchor():
    tile = Tile("TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))
    assert tile.right() == "GCTGAGAAGAGG"
    assert tile.right_c() == "CGACTCTTCTCC"
