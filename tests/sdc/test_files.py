
from sdc.tile import TileManager
from sdc.files import write_sdc_tileset, read_sdc_tileset


TA0 = TileManager(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12)).next()                       #  A0*
TA1 = TileManager(0, "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12)).next()                       #  A2*
TB0 = TileManager(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()                       # 0B0*
TB1 = TileManager(1, "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT").next()                       # 2B2*
TC0 = TileManager(2, "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG").next()                       # 0C0*
TC1 = TileManager(2, "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA").next()                       # 2C2*
TDQ = TileManager(3, "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)).next() # 0DQ*
TD  = TileManager(3, "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0)).next()                       # 2D

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
TK  = TileManager(11, "TCTTTCCAAGCC ATTAGAGAGTACCTTTAATTGCTC", (12, 24, 0)).next()


BITCOPY_04POS_0_TILES = [ [ TA0 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TDQ, TD ] ]
BITCOPY_04POS_1_TILES = [ [ TA1 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TDQ, TD ] ]
BITCOPY_11POS_0_TILES = [ [ TA0 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TD0, TD1 ], [ TE0, TE1 ], [ Tf0, Tf1 ], [ TF0, TF1 ], [ TG0, TG1 ], [ TH0, TH1 ], [ TI0, TI1 ], [ TJ0, TJ1 ], [ TKQ, TK ] ]
BITCOPY_11POS_1_TILES = [ [ TA1 ], [ TB0, TB1 ], [ TC0, TC1 ], [ TD0, TD1 ], [ TE0, TE1 ], [ Tf0, Tf1 ], [ TF0, TF1 ], [ TG0, TG1 ], [ TH0, TH1 ], [ TI0, TI1 ], [ TJ0, TJ1 ], [ TKQ, TK ] ]




def test_write_read_json__bitcopy_04pos_0():
    write_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json", BITCOPY_04POS_0_TILES)
    assert read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json") == BITCOPY_04POS_0_TILES

def test_write_read_json__bitcopy_04pos_1():
    write_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json", BITCOPY_04POS_1_TILES)
    assert read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json") == BITCOPY_04POS_1_TILES



def test_write_read_json__bitcopy_11pos_0():
    write_sdc_tileset("./data/sdc/1D/bitcopy_11pos_0.json", BITCOPY_11POS_0_TILES)
    assert read_sdc_tileset("./data/sdc/1D/bitcopy_11pos_0.json") == BITCOPY_11POS_0_TILES

def test_write_read_json__bitcopy_11pos_1():
    write_sdc_tileset("./data/sdc/1D/bitcopy_11pos_1.json", BITCOPY_11POS_1_TILES)
    assert read_sdc_tileset("./data/sdc/1D/bitcopy_11pos_1.json") == BITCOPY_11POS_1_TILES


