
from sdc.builders import TileBuilder


def test_equality():
    a = TileBuilder(1, "GCTGAGAAGAGG").build()
    b = TileBuilder(1, "GCTGAGAAGAGG").build()
    c = TileBuilder(1, "GCTGAGAAGAGG", layout = (4, 4, 4)).build()
    d = TileBuilder(1, "AACAGGGATGTG", layout = (0, 8, 4)).build()
    e = TileBuilder(1, "AACAGGGATGTG", layout = (4, 8, 0)).build()

    assert a == b
    assert a != c
    assert a != d
    assert a != e


def test_anchor():
    tile = TileBuilder(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12)).build()
    assert tile.get_right() == "GCTGAGAAGAGG"
    assert tile.get_right_complement() == "CGACTCTTCTCC"


def test_left():
    tile = TileBuilder(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").build()
    assert tile.get_left() == "CCTCTTCTCAGC"
    assert tile.get_left_complement() == "GGAGAAGAGTCG"


def test_middle():
    tile = TileBuilder(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").build()
    assert tile.get_middle() == "AGCGTCCAATACTGCGGAATCGTC"
    assert tile.get_middle_complement() == "TCGCAGGTTATGACGCCTTAGCAG"


def test_right():
    tile = TileBuilder(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").build()
    assert tile.get_right() == "GGTCAGGATGAG"
    assert tile.get_right_complement() == "CCAGTCCTACTC"

def test_sentinel():
    tile = TileBuilder (1, "", layout = (0, 0, 0), concentration = 1).build()
    assert tile.get_left() == ""
    assert tile.get_middle() == ""
    assert tile.get_right() == ""
