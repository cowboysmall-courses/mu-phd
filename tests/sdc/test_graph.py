
import math

from sdc.files import read_sdc_tileset
from sdc.graph import SDCGraph
from sdc.tile import Tile


TA0 = Tile(0,  "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))                       #  A0*
TA1 = Tile(0,  "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12))                       #  A2*
TB0 = Tile(1,  "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")                       # 0B0*
TB1 = Tile(1,  "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT")                       # 2B2*
TC0 = Tile(2,  "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG")                       # 0C0*
TC1 = Tile(2,  "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA")                       # 2C2*
TDQ = Tile(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)) # 0DQ*
TD  = Tile(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0))                       # 2D

TD0 = Tile(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG")                       # 0D0*
TD1 = Tile(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA AATGGTGGCATT")                       # 2D2*
TE0 = Tile(4,  "CTCATCCTGACC CGAGAATGACCATAAATCAAAAAT GCTGAGAAGAGG")                       # 0E0*
TE1 = Tile(4,  "AATGCCACCATT CGAGAATGACCATAAATCAAAAAT GGCTTGGAAAGA")                       # 2E2*
Tf0 = Tile(5,  "CCTCTTCTCAGC CAGGTCTTTACCCTGACTATTATA GGTCAGGATGAG")                       # 0f0*
Tf1 = Tile(5,  "TCTTTCCAAGCC CAGGTCTTTACCCTGACTATTATA AATGGTGGCATT")                       # 2f2*
TF0 = Tile(6,  "CTCATCCTGACC GTCAGAAGCAAAGCGGATTGCATC GCTGAGAAGAGG")                       # 0F0*
TF1 = Tile(6,  "AATGCCACCATT GTCAGAAGCAAAGCGGATTGCATC GGCTTGGAAAGA")                       # 2F2*
TG0 = Tile(7,  "CCTCTTCTCAGC AAAAAGATTAAGAGGAAGCCCGAA GGTCAGGATGAG")                       # 0G0*
TG1 = Tile(7,  "TCTTTCCAAGCC AAAAAGATTAAGAGGAAGCCCGAA AATGGTGGCATT")                       # 2G2*
TH0 = Tile(8,  "CTCATCCTGACC AGACTTCAAATATCGCGTTTTAAT GCTGAGAAGAGG")                       # 0H0*
TH1 = Tile(8,  "AATGCCACCATT AGACTTCAAATATCGCGTTTTAAT GGCTTGGAAAGA")                       # 2H2*
TI0 = Tile(9,  "CCTCTTCTCAGC TCGAGCTTCAAAGCGAACCAGACC GGTCAGGATGAG")                       # 0I0*
TI1 = Tile(9,  "TCTTTCCAAGCC TCGAGCTTCAAAGCGAACCAGACC AATGGTGGCATT")                       # 2I2*
TJ0 = Tile(10, "CTCATCCTGACC GGAAGCAAACTCCAACAGGTCAGG GCTGAGAAGAGG")                       # 0J0*
TJ1 = Tile(10, "AATGCCACCATT GGAAGCAAACTCCAACAGGTCAGG GGCTTGGAAAGA")                       # 2J2*
TKQ = Tile(11, "CCTCTTCTCAGC ATTAGAGAGTACCTTTAATTGCTC GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)) # 0KQ*
TK  = Tile(11, "TCTTTCCAAGCC ATTAGAGAGTACCTTTAATTGCTC", (12, 24, 0))                       # 2K



def test_graph__bitcopy_4pos_0():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).shortest_path(TA0, 273.15 + 37)
    assert math.isclose(mfe, -152.454, abs_tol = 0.001)
    assert path == [TA0, TB0, TC0, TDQ]

def test_graph__bitcopy_4pos_1():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos.json")).shortest_path(TA1, 273.15 + 37)
    assert math.isclose(mfe, -152.103, abs_tol = 0.001)
    assert path == [TA1, TB1, TC1, TD]



def test_graph__bitcopy_11pos_0():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos.json")).shortest_path(TA0, 273.15 + 37)
    assert math.isclose(mfe, -484.441, abs_tol = 0.001)
    assert path == [TA0, TB0, TC0, TD0, TE0, Tf0, TF0, TG0, TH0, TI0, TJ0, TKQ]

def test_graph__bitcopy_11pos_1():
    mfe, path = SDCGraph(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos.json")).shortest_path(TA1, 273.15 + 37)
    assert math.isclose(mfe, -483.219, abs_tol = 0.001)
    assert path == [TA1, TB1, TC1, TD1, TE1, Tf1, TF1, TG1, TH1, TI1, TJ1, TK]
