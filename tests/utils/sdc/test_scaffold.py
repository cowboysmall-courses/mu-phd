
from utils.sdc.scaffold import Scaffold


def test_get_positions__exits():
    scaffold = Scaffold("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA")

    assert "ATTTTTGATTTATGGTCATTCTCG" in scaffold.get_positions()
    assert "TTTTCTGAACTGTTTAAAGCATTT" in scaffold.get_positions()
    assert "GAGGGGGATTCAATGAATATTTAT" in scaffold.get_positions()
    assert "GACGATTCCGCAGTATTGGACGCT" in scaffold.get_positions()
    assert "CTGGCAAATTAGGCTCTGGAAAGA" in scaffold.get_positions()


def test_get_positions__index():
    scaffold = Scaffold("ATTTTTGATTTATGGTCATTCTCG TTTTCTGAACTGTTTAAAGCATTT GAGGGGGATTCAATGAATATTTAT GACGATTCCGCAGTATTGGACGCT CTGGCAAATTAGGCTCTGGAAAGA")

    assert scaffold.get_positions()["ATTTTTGATTTATGGTCATTCTCG"] == 0
    assert scaffold.get_positions()["TTTTCTGAACTGTTTAAAGCATTT"] == 1
    assert scaffold.get_positions()["GAGGGGGATTCAATGAATATTTAT"] == 2
    assert scaffold.get_positions()["GACGATTCCGCAGTATTGGACGCT"] == 3
    assert scaffold.get_positions()["CTGGCAAATTAGGCTCTGGAAAGA"] == 4

