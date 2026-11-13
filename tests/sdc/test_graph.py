
from sdc.builders import TileBuilder
from sdc.files import read_sdc_tileset
from sdc.graph import SDCGraph

import math


TA0 = TileBuilder(0,  "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12)).build()                       #  A0*
TA1 = TileBuilder(0,  "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12)).build()                       #  A2*
TB0 = TileBuilder(1,  "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").build()                       # 0B0*
TB1 = TileBuilder(1,  "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT").build()                       # 2B2*
TC0 = TileBuilder(2,  "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG").build()                       # 0C0*
TC1 = TileBuilder(2,  "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA").build()                       # 2C2*
TDQ = TileBuilder(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)).build() # 0DQ*
TD  = TileBuilder(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0)).build()                       # 2D

TD0 = TileBuilder(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG").build()                       # 0D0*
TD1 = TileBuilder(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA AATGGTGGCATT").build()                       # 2D2*
TE0 = TileBuilder(4,  "CTCATCCTGACC CGAGAATGACCATAAATCAAAAAT GCTGAGAAGAGG").build()                       # 0E0*
TE1 = TileBuilder(4,  "AATGCCACCATT CGAGAATGACCATAAATCAAAAAT GGCTTGGAAAGA").build()                       # 2E2*
Tf0 = TileBuilder(5,  "CCTCTTCTCAGC CAGGTCTTTACCCTGACTATTATA GGTCAGGATGAG").build()                       # 0f0*
Tf1 = TileBuilder(5,  "TCTTTCCAAGCC CAGGTCTTTACCCTGACTATTATA AATGGTGGCATT").build()                       # 2f2*
TF0 = TileBuilder(6,  "CTCATCCTGACC GTCAGAAGCAAAGCGGATTGCATC GCTGAGAAGAGG").build()                       # 0F0*
TF1 = TileBuilder(6,  "AATGCCACCATT GTCAGAAGCAAAGCGGATTGCATC GGCTTGGAAAGA").build()                       # 2F2*
TG0 = TileBuilder(7,  "CCTCTTCTCAGC AAAAAGATTAAGAGGAAGCCCGAA GGTCAGGATGAG").build()                       # 0G0*
TG1 = TileBuilder(7,  "TCTTTCCAAGCC AAAAAGATTAAGAGGAAGCCCGAA AATGGTGGCATT").build()                       # 2G2*
TH0 = TileBuilder(8,  "CTCATCCTGACC AGACTTCAAATATCGCGTTTTAAT GCTGAGAAGAGG").build()                       # 0H0*
TH1 = TileBuilder(8,  "AATGCCACCATT AGACTTCAAATATCGCGTTTTAAT GGCTTGGAAAGA").build()                       # 2H2*
TI0 = TileBuilder(9,  "CCTCTTCTCAGC TCGAGCTTCAAAGCGAACCAGACC GGTCAGGATGAG").build()                       # 0I0*
TI1 = TileBuilder(9,  "TCTTTCCAAGCC TCGAGCTTCAAAGCGAACCAGACC AATGGTGGCATT").build()                       # 2I2*
TJ0 = TileBuilder(10, "CTCATCCTGACC GGAAGCAAACTCCAACAGGTCAGG GCTGAGAAGAGG").build()                       # 0J0*
TJ1 = TileBuilder(10, "AATGCCACCATT GGAAGCAAACTCCAACAGGTCAGG GGCTTGGAAAGA").build()                       # 2J2*
TKQ = TileBuilder(11, "CCTCTTCTCAGC ATTAGAGAGTACCTTTAATTGCTC GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)).build() # 0KQ*
TK  = TileBuilder(11, "TCTTTCCAAGCC ATTAGAGAGTACCTTTAATTGCTC", (12, 24, 0)).build()                       # 2K



def test_minimum_free_energy__bitcopy_4pos_0():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")]
    mfe, path = SDCGraph(tileset).minimum_free_energy(TA0, 273.15 + 37)
    assert math.isclose(mfe, -152.454, abs_tol = 0.001)
    assert path == [TA0, TB0, TC0, TDQ]

def test_minimum_free_energy__bitcopy_4pos_1():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")]
    mfe, path = SDCGraph(tileset).minimum_free_energy(TA1, 273.15 + 37)
    assert math.isclose(mfe, -152.103, abs_tol = 0.001)
    assert path == [TA1, TB1, TC1, TD]



def test_minimum_free_energy__bitcopy_11pos_0():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos.json")]
    mfe, path = SDCGraph(tileset).minimum_free_energy(TA0, 273.15 + 37)
    assert math.isclose(mfe, -484.441, abs_tol = 0.001)
    assert path == [TA0, TB0, TC0, TD0, TE0, Tf0, TF0, TG0, TH0, TI0, TJ0, TKQ]

def test_minimum_free_energy__bitcopy_11pos_1():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos.json")]
    mfe, path = SDCGraph(tileset).minimum_free_energy(TA1, 273.15 + 37)
    assert math.isclose(mfe, -483.219, abs_tol = 0.001)
    assert path == [TA1, TB1, TC1, TD1, TE1, Tf1, TF1, TG1, TH1, TI1, TJ1, TK]



def test_configuration_free_energy__bitcopy_4pos_0():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")]
    E = SDCGraph(tileset).configuration_free_energy((1, 1, 1, 1), 273.15 + 37)
    assert math.isclose(E, -152.454, abs_tol = 0.001)

def test_configuration_free_energy__bitcopy_4pos_1():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")]
    E = SDCGraph(tileset).configuration_free_energy((2, 2, 2, 2), 273.15 + 37)
    assert math.isclose(E, -152.103, abs_tol = 0.001)



def test_tiles_free_energy__bitcopy_4pos_0():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")]
    E = SDCGraph(tileset).tiles_free_energy([TA0, TB0, TC0, TDQ], 273.15 + 37)
    assert math.isclose(E, -152.454, abs_tol = 0.001)

def test_tiles_free_energy__bitcopy_4pos_1():
    # tileset = read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")
    tileset = [[builder.build() for builder in layer] for layer in read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos.json")]
    E = SDCGraph(tileset).tiles_free_energy([TA1, TB1, TC1, TD], 273.15 + 37)
    assert math.isclose(E, -152.103, abs_tol = 0.001)

