
from sdc.builders import ScaffoldBuilder, TileBuilder
from sdc.files import write_sdc_tileset, read_sdc_tileset


S0 = ScaffoldBuilder("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA")

TA0 = TileBuilder(0,  "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))                       #  A0*
TA1 = TileBuilder(0,  "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12))                       #  A2*
TB0 = TileBuilder(1,  "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")                       # 0B0*
TB1 = TileBuilder(1,  "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT")                       # 2B2*
TC0 = TileBuilder(2,  "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG")                       # 0C0*
TC1 = TileBuilder(2,  "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA")                       # 2C2*
TDQ = TileBuilder(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)) # 0DQ*
TD  = TileBuilder(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0))                       # 2D

TD0 = TileBuilder(3,  "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG")                       # 0D0*
TD1 = TileBuilder(3,  "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA AATGGTGGCATT")                       # 2D2*
TE0 = TileBuilder(4,  "CTCATCCTGACC CGAGAATGACCATAAATCAAAAAT GCTGAGAAGAGG")                       # 0E0*
TE1 = TileBuilder(4,  "AATGCCACCATT CGAGAATGACCATAAATCAAAAAT GGCTTGGAAAGA")                       # 2E2*
Tf0 = TileBuilder(5,  "CCTCTTCTCAGC CAGGTCTTTACCCTGACTATTATA GGTCAGGATGAG")                       # 0f0*
Tf1 = TileBuilder(5,  "TCTTTCCAAGCC CAGGTCTTTACCCTGACTATTATA AATGGTGGCATT")                       # 2f2*
TF0 = TileBuilder(6,  "CTCATCCTGACC GTCAGAAGCAAAGCGGATTGCATC GCTGAGAAGAGG")                       # 0F0*
TF1 = TileBuilder(6,  "AATGCCACCATT GTCAGAAGCAAAGCGGATTGCATC GGCTTGGAAAGA")                       # 2F2*
TG0 = TileBuilder(7,  "CCTCTTCTCAGC AAAAAGATTAAGAGGAAGCCCGAA GGTCAGGATGAG")                       # 0G0*
TG1 = TileBuilder(7,  "TCTTTCCAAGCC AAAAAGATTAAGAGGAAGCCCGAA AATGGTGGCATT")                       # 2G2*
TH0 = TileBuilder(8,  "CTCATCCTGACC AGACTTCAAATATCGCGTTTTAAT GCTGAGAAGAGG")                       # 0H0*
TH1 = TileBuilder(8,  "AATGCCACCATT AGACTTCAAATATCGCGTTTTAAT GGCTTGGAAAGA")                       # 2H2*
TI0 = TileBuilder(9,  "CCTCTTCTCAGC TCGAGCTTCAAAGCGAACCAGACC GGTCAGGATGAG")                       # 0I0*
TI1 = TileBuilder(9,  "TCTTTCCAAGCC TCGAGCTTCAAAGCGAACCAGACC AATGGTGGCATT")                       # 2I2*
TJ0 = TileBuilder(10, "CTCATCCTGACC GGAAGCAAACTCCAACAGGTCAGG GCTGAGAAGAGG")                       # 0J0*
TJ1 = TileBuilder(10, "AATGCCACCATT GGAAGCAAACTCCAACAGGTCAGG GGCTTGGAAAGA")                       # 2J2*
TKQ = TileBuilder(11, "CCTCTTCTCAGC ATTAGAGAGTACCTTTAATTGCTC GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)) # 0KQ*
TK  = TileBuilder(11, "TCTTTCCAAGCC ATTAGAGAGTACCTTTAATTGCTC", (12, 24, 0))                       # 2K


BITCOPY_04POS_0_TILES = [ [ TA0 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TDQ, TD ] ]
BITCOPY_04POS_1_TILES = [ [ TA1 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TDQ, TD ] ]
BITCOPY_11POS_0_TILES = [ [ TA0 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TD0, TD1 ], [ TE0, TE1 ], [ Tf0, Tf1 ], [ TF0, TF1 ], [ TG0, TG1 ], [ TH0, TH1 ], [ TI0, TI1 ], [ TJ0, TJ1 ], [ TKQ, TK ] ]
BITCOPY_11POS_1_TILES = [ [ TA1 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TD0, TD1 ], [ TE0, TE1 ], [ Tf0, Tf1 ], [ TF0, TF1 ], [ TG0, TG1 ], [ TH0, TH1 ], [ TI0, TI1 ], [ TJ0, TJ1 ], [ TKQ, TK ] ]




def test_write_read_json__bitcopy_04pos_0():
    write_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos_0.json", BITCOPY_04POS_0_TILES)
    assert read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos_0.json") == BITCOPY_04POS_0_TILES

def test_write_read_json__bitcopy_04pos_1():
    write_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos_1.json", BITCOPY_04POS_1_TILES)
    assert read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_04pos_1.json") == BITCOPY_04POS_1_TILES



def test_write_read_json__bitcopy_11pos_0():
    write_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos_0.json", BITCOPY_11POS_0_TILES)
    assert read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos_0.json") == BITCOPY_11POS_0_TILES

def test_write_read_json__bitcopy_11pos_1():
    write_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos_1.json", BITCOPY_11POS_1_TILES)
    assert read_sdc_tileset("./data/sdc/1D/tiles/bitcopy_11pos_1.json") == BITCOPY_11POS_1_TILES


