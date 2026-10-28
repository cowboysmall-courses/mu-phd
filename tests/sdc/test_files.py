
from sdc.tile import Tile
from sdc.files import write_sdc_tileset, read_sdc_tileset


TA0 = Tile(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", (0, 24, 12))                       #  A0*
TA1 = Tile(0, "TCTTTCCAGAGCCTAATTTGCCAG GGCTTGGAAAGA", (0, 24, 12))                       #  A2*
TB0 = Tile(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")                       # 0B0*
TB1 = Tile(1, "TCTTTCCAAGCC AGCGTCCAATACTGCGGAATCGTC AATGGTGGCATT")                       # 2B2*
TC0 = Tile(2, "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG")                       # 0C0*
TC1 = Tile(2, "AATGCCACCATT ATAAATATTCATTGAATCCCCCTC GGCTTGGAAAGA")                       # 2C2*
TDQ = Tile(3, "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGGTAGTGTGGAGAGGTGGG", (12, 24, 20)) # 0DQ*
TD  = Tile(3, "TCTTTCCAAGCC AAATGCTTTAAACAGTTCAGAAAA", (12, 24, 0))                       # 2D


BITCOPY_0_TILES = { 0: [ TA0 ], 1: [ TB0, TB1 ], 2: [ TC0, TC1 ], 3: [ TDQ, TD ] }
BITCOPY_1_TILES = { 0: [ TA1 ], 1: [ TB0, TB1 ], 2: [ TC0, TC1 ], 3: [ TDQ, TD ] }



def test_write_read_json__bitcopy_0():
    write_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json", BITCOPY_0_TILES)
    assert read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json") == BITCOPY_0_TILES

def test_write_read_json__bitcopy_1():
    write_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json", BITCOPY_1_TILES)
    assert read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json") == BITCOPY_1_TILES

