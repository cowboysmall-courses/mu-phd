
from sdc.managers import ScaffoldManager
from sdc.tile import NullTile, TileManager


def test_get_positions__exits():
    scaffold = ScaffoldManager("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA").next()

    assert "GCTCTTACTGGTATTTAGTTTTTA" in scaffold.get_positions()
    assert "TTTACGAAATTTGTCAAGTCTTTT" in scaffold.get_positions()
    assert "TATTTATAAGTAACTTAGGGGGAG" in scaffold.get_positions()
    assert "TCGCAGGTTATGACGCCTTAGCAG" in scaffold.get_positions()
    assert "AGAAAGGTCTCGGATTAAACGGTC" in scaffold.get_positions()


def test_get_position_index():
    scaffold = ScaffoldManager("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA").next()

    assert scaffold.get_position_index("AGAAAGGTCTCGGATTAAACGGTC") == 0
    assert scaffold.get_position_index("TCGCAGGTTATGACGCCTTAGCAG") == 1
    assert scaffold.get_position_index("TATTTATAAGTAACTTAGGGGGAG") == 2
    assert scaffold.get_position_index("TTTACGAAATTTGTCAAGTCTTTT") == 3
    assert scaffold.get_position_index("GCTCTTACTGGTATTTAGTTTTTA") == 4


def test_bind():
    scaffold = ScaffoldManager("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA").next()

    tile1 = TileManager(0, "TCTTTCCAGAGCCTAATTTGCCAG GCTGAGAAGAGG", layout = (0, 24, 12)).next()
    tile2 = TileManager(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()
    tile3 = TileManager(2, "CTCATCCTGACC ATAAATATTCATTGAATCCCCCTC GCTGAGAAGAGG").next()
    tile4 = TileManager(3, "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG").next()

    assert scaffold.is_position_free(tile1)
    assert scaffold.is_position_free(tile2)
    assert scaffold.is_position_free(tile3)
    assert scaffold.is_position_free(tile4)

    scaffold.bind(tile1)
    scaffold.bind(tile2)
    scaffold.bind(tile3)
    scaffold.bind(tile4)

    assert scaffold.is_position_taken(tile1)
    assert scaffold.is_position_taken(tile2)
    assert scaffold.is_position_taken(tile3)
    assert scaffold.is_position_taken(tile4)


def test_get_bound_tiles():
    scaffold = ScaffoldManager("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA").next()

    tile2 = TileManager(1, "CCTCTTCTCAGC AGCGTCCAATACTGCGGAATCGTC GGTCAGGATGAG").next()
    tile4 = TileManager(3, "CCTCTTCTCAGC AAATGCTTTAAACAGTTCAGAAAA GGTCAGGATGAG").next()

    scaffold.bind(tile2)
    scaffold.bind(tile4)

    tiles = scaffold.get_bound_tiles()

    assert tiles == [NullTile(0), tile2, NullTile(2), tile4, NullTile(4)]


