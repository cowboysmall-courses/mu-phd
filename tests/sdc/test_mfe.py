
import math

from sdc.mfe import minimum_free_energy, minimum_free_energy_configuration, minimum_free_energy_path, partition_function
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



def test_partition_function__bitcopy_0():
    assert math.isclose(partition_function(BITCOPY_0_TILES, 273.15 + 37), 53.719, abs_tol = 0.001)


def test_partition_function__bitcopy_1():
    assert math.isclose(partition_function(BITCOPY_1_TILES, 273.15 + 37), 53.727, abs_tol = 0.001)



def test_minimum_free_energy__bitcopy_0():
    assert math.isclose(minimum_free_energy(BITCOPY_0_TILES, 273.15 + 37), -152.454, abs_tol = 0.001)


def test_minimum_free_energy__bitcopy_1():
    assert math.isclose(minimum_free_energy(BITCOPY_1_TILES, 273.15 + 37), -152.103, abs_tol = 0.001)



def test_minimum_free_energy_configuration__bitcopy_0():
    assert minimum_free_energy_configuration(BITCOPY_0_TILES, 273.15 + 37) == [TA0, TB0, TC0, TDQ]


def test_minimum_free_energy_configuration__bitcopy_1():
    assert minimum_free_energy_configuration(BITCOPY_1_TILES, 273.15 + 37) == [TA1, TB1, TC1, TD]



def test_minimum_free_energy_path__bitcopy_0():
    assert minimum_free_energy_path(BITCOPY_0_TILES, 273.15 + 37) == [((0, 0), (1, 0)), ((1, 0), (2, 0)), ((2, 0), (3, 0))]


def test_minimum_free_energy_path__bitcopy_1():
    assert minimum_free_energy_path(BITCOPY_1_TILES, 273.15 + 37) == [((0, 0), (1, 1)), ((1, 1), (2, 1)), ((2, 1), (3, 1))]

