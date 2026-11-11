
from sdc.tile import TileManager


def test_equality():
    a = TileManager(1, "GCTGAGAAGAGG").next()
    b = TileManager(1, "GCTGAGAAGAGG").next()
    c = TileManager(1, "GCTGAGAAGAGG", layout = (4, 4, 4)).next()
    d = TileManager(1, "AACAGGGATGTG", layout = (0, 8, 4)).next()
    e = TileManager(1, "AACAGGGATGTG", layout = (4, 8, 0)).next()

    assert a == b
    assert a != c
    assert a != d
    assert a != e


def test_anchor():
    tile = TileManager(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12)).next()
    assert tile.get_right() == "GCTGAGAAGAGG"
    assert tile.get_right_complement() == "CGACTCTTCTCC"


def test_left():
    tile = TileManager(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()
    assert tile.get_left() == "CCTCTTCTCAGC"
    assert tile.get_left_complement() == "GGAGAAGAGTCG"


def test_middle():
    tile = TileManager(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()
    assert tile.get_middle() == "AGCGTCCAATACTGCGGAATCGTC"
    assert tile.get_middle_complement() == "TCGCAGGTTATGACGCCTTAGCAG"


def test_right():
    tile = TileManager(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()
    assert tile.get_right() == "GGTCAGGATGAG"
    assert tile.get_right_complement() == "CCAGTCCTACTC"

def test_sentinel():
    tile = TileManager (1, "", layout = (0, 0, 0), concentration = 1).next()
    assert tile.get_left() == ""
    assert tile.get_middle() == ""
    assert tile.get_right() == ""
