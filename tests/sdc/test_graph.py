
import math

from sdc.graph import SDCGraph
from sdc.tile import Tile


TA0 = Tile(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))
TA1 = Tile(0, "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12))

TB0 = Tile(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
TB1 = Tile(1, "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT")

TC0 = Tile(2, "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG")
TC1 = Tile(2, "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA")

TDQ = Tile(3, "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20))
TD  = Tile(3, "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0))


BITCOPY_0_TILES = {

    0: [
        TA0   #  A0*
    ],

    1: [
        TB0,  # 0B0*
        TB1   # 2B2*
    ],

    2: [
        TC0,  # 0C0*
        TC1   # 2C2*
    ],

    3: [
        TDQ,  # 0DQ*
        TD    # 2D
    ]
}

BITCOPY_1_TILES = {

    0: [
        TA1,  #  A2*
    ],

    1: [
        TB0,  # 0B0
        TB1   # 2B2*
    ],

    2: [
        TC0,  # 0C0*
        TC1   # 2C2*
    ],

    3: [
        TDQ,  # 0DQ*
        TD    # 2D
    ]
}



def test_graph__bitcopy_0():
    graph = SDCGraph(BITCOPY_0_TILES)
    assert graph.shortest_path(TA0, 273.15 + 37) != {}

def test_graph__bitcopy_1():
    graph = SDCGraph(BITCOPY_1_TILES)
    assert graph.shortest_path(TA1, 273.15 + 37) != {}

