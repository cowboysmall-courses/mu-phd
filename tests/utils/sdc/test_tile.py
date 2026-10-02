
from utils.sdc.tile import Tile


def test_equality():
    a = Tile("GCTGAGAAGAGG")
    b = Tile("GCTGAGAAGAGG")
    c = Tile("GCTGAGAAGAGG", (4, 4, 4))
    d = Tile("AACAGGGATGTG")
    e = Tile("AACAGGGATGTG", (4, 4, 4))

    assert a == b
    assert a != c
    assert a != d
    assert a != e


def test_left():
    tile = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.left() == "CCTCTTCTCAGC"


def test_position():
    tile = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.position() == "AGCGTCCAATACTGCGGAATCGTC"


def test_right():
    tile = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    assert tile.right() == "GGTCAGGATGAG"
