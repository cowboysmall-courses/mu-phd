
from utils.sdc.scaffold import Scaffold
from utils.sdc.tile import Tile


def test_get_positions__exits():
    scaffold = Scaffold("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA")

    assert "GCTCTTACTGGTATTTAGTTTTTA" in scaffold.get_positions()
    assert "TTTACGAAATTTGTCAAGTCTTTT" in scaffold.get_positions()
    assert "TATTTATAAGTAACTTAGGGGGAG" in scaffold.get_positions()
    assert "TCGCAGGTTATGACGCCTTAGCAG" in scaffold.get_positions()
    assert "AGAAAGGTCTCGGATTAAACGGTC" in scaffold.get_positions()


def test_get_position_index():
    scaffold = Scaffold("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA")

    assert scaffold.get_position_index("AGAAAGGTCTCGGATTAAACGGTC") == 0
    assert scaffold.get_position_index("TCGCAGGTTATGACGCCTTAGCAG") == 1
    assert scaffold.get_position_index("TATTTATAAGTAACTTAGGGGGAG") == 2
    assert scaffold.get_position_index("TTTACGAAATTTGTCAAGTCTTTT") == 3
    assert scaffold.get_position_index("GCTCTTACTGGTATTTAGTTTTTA") == 4


def test_bind():
    scaffold = Scaffold("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA")

    tile1 = Tile("TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", layout = (0, 24, 12))
    tile2 = Tile("CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG")
    tile3 = Tile("CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG")
    tile4 = Tile("CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG")


    assert scaffold.is_free(tile1)
    assert scaffold.is_free(tile2)
    assert scaffold.is_free(tile3)
    assert scaffold.is_free(tile4)

    scaffold.bind(tile1)
    scaffold.bind(tile2)
    scaffold.bind(tile3)
    scaffold.bind(tile4)

    assert scaffold.is_taken(tile1)
    assert scaffold.is_taken(tile2)
    assert scaffold.is_taken(tile3)
    assert scaffold.is_taken(tile4)
