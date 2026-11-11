
from sdc.files import read_sdc_tileset
from sdc.graph import SDCGraph
from sdc.tile import TileManager

import math


TA0 = TileManager(0,  "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12)).next()                       #  A0*
TA1 = TileManager(0,  "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12)).next()                       #  A2*
TB0 = TileManager(1,  "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()                       # 0B0*
TB1 = TileManager(1,  "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT").next()                       # 2B2*
TC0 = TileManager(2,  "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG").next()                       # 0C0*
TC1 = TileManager(2,  "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA").next()                       # 2C2*
TDQ = TileManager(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)).next() # 0DQ*
TD  = TileManager(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0)).next()                       # 2D

TD0 = TileManager(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG").next()                       # 0D0*
TD1 = TileManager(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA AATGGTGGCATT").next()                       # 2D2*
TE0 = TileManager(4,  "CTCATCCTGACC CGAGAATGACCATAAATCAAAAAT GCTGAGAAGAGG").next()                       # 0E0*
TE1 = TileManager(4,  "AATGCCACCATT CGAGAATGACCATAAATCAAAAAT GGCTTGGAAAGA").next()                       # 2E2*
Tf0 = TileManager(5,  "CCTCTTCTCAGC CAGGTCTTTACCCTGACTATTATA GGTCAGGATGAG").next()                       # 0f0*
Tf1 = TileManager(5,  "TCTTTCCAAGCC CAGGTCTTTACCCTGACTATTATA AATGGTGGCATT").next()                       # 2f2*
TF0 = TileManager(6,  "CTCATCCTGACC GTCAGAAGCAAAGCGGATTGCATC GCTGAGAAGAGG").next()                       # 0F0*
TF1 = TileManager(6,  "AATGCCACCATT GTCAGAAGCAAAGCGGATTGCATC GGCTTGGAAAGA").next()                       # 2F2*
TG0 = TileManager(7,  "CCTCTTCTCAGC AAAAAGATTAAGAGGAAGCCCGAA GGTCAGGATGAG").next()                       # 0G0*
TG1 = TileManager(7,  "TCTTTCCAAGCC AAAAAGATTAAGAGGAAGCCCGAA AATGGTGGCATT").next()                       # 2G2*
TH0 = TileManager(8,  "CTCATCCTGACC AGACTTCAAATATCGCGTTTTAAT GCTGAGAAGAGG").next()                       # 0H0*
TH1 = TileManager(8,  "AATGCCACCATT AGACTTCAAATATCGCGTTTTAAT GGCTTGGAAAGA").next()                       # 2H2*
TI0 = TileManager(9,  "CCTCTTCTCAGC TCGAGCTTCAAAGCGAACCAGACC GGTCAGGATGAG").next()                       # 0I0*
TI1 = TileManager(9,  "TCTTTCCAAGCC TCGAGCTTCAAAGCGAACCAGACC AATGGTGGCATT").next()                       # 2I2*
TJ0 = TileManager(10, "CTCATCCTGACC GGAAGCAAACTCCAACAGGTCAGG GCTGAGAAGAGG").next()                       # 0J0*
TJ1 = TileManager(10, "AATGCCACCATT GGAAGCAAACTCCAACAGGTCAGG GGCTTGGAAAGA").next()                       # 2J2*
TKQ = TileManager(11, "CCTCTTCTCAGC ATTAGAGAGTACCTTTAATTGCTC GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)).next() # 0KQ*
TK  = TileManager(11, "TCTTTCCAAGCC ATTAGAGAGTACCTTTAATTGCTC", (12, 24, 0)).next()                       # 2K



def test_minimum_free_energy__bitcopy_4pos_0():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).minimum_free_energy(TA0, 273.15 + 37)
    assert math.isclose(mfe, -152.454, abs_tol = 0.001)
    assert path == [TA0, TB0, TC0, TDQ]

def test_minimum_free_energy__bitcopy_4pos_1():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).minimum_free_energy(TA1, 273.15 + 37)
    assert math.isclose(mfe, -152.103, abs_tol = 0.001)
    assert path == [TA1, TB1, TC1, TD]



def test_minimum_free_energy__bitcopy_11pos_0():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos.json")).minimum_free_energy(TA0, 273.15 + 37)
    assert math.isclose(mfe, -484.441, abs_tol = 0.001)
    assert path == [TA0, TB0, TC0, TD0, TE0, Tf0, TF0, TG0, TH0, TI0, TJ0, TKQ]

def test_minimum_free_energy__bitcopy_11pos_1():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos.json")).minimum_free_energy(TA1, 273.15 + 37)
    assert math.isclose(mfe, -483.219, abs_tol = 0.001)
    assert path == [TA1, TB1, TC1, TD1, TE1, Tf1, TF1, TG1, TH1, TI1, TJ1, TK]



def test_configuration_free_energy__bitcopy_4pos_0():
    E = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).configuration_free_energy((1, 1, 1, 1), 273.15 + 37)
    assert math.isclose(E, -152.454, abs_tol = 0.001)

def test_configuration_free_energy__bitcopy_4pos_1():
    E = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).configuration_free_energy((2, 2, 2, 2), 273.15 + 37)
    assert math.isclose(E, -152.103, abs_tol = 0.001)



def test_tiles_free_energy__bitcopy_4pos_0():
    E = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).tiles_free_energy([TA0, TB0, TC0, TDQ], 273.15 + 37)
    assert math.isclose(E, -152.454, abs_tol = 0.001)

def test_tiles_free_energy__bitcopy_4pos_1():
    E = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).tiles_free_energy([TA1, TB1, TC1, TD], 273.15 + 37)
    assert math.isclose(E, -152.103, abs_tol = 0.001)

