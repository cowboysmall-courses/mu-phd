
from sdc.mfe import minimum_free_energy_configuration
from sdc.tile import Tile


TA0 = Tile("TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))
TA1 = Tile("TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12))

TB0 = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
TB1 = Tile("TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT")

TC0 = Tile("CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG")
TC1 = Tile("AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA")

TDQ = Tile("CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20))
TD  = Tile("TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0))


BITCOPY_0_TILES = {

    0: [
        TA0   #  A0*
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


def test_minimum_free_energy_configuration__bitcopy_0():
    assert minimum_free_energy_configuration(BITCOPY_0_TILES, 363) == [TA0, TB0, TC0, TDQ]

def test_minimum_free_energy_configuration__bitcopy_1():
    assert minimum_free_energy_configuration(BITCOPY_1_TILES, 353) == [TA1, TB1, TC1, TD]
