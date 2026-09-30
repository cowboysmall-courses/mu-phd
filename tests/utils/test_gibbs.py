
import math

from utils.gibbs import free_energy


def test_free_energy__no_mismatches():
    assert math.isclose(free_energy("CGTTGA", "GCAACT", 310.15), -5.357, abs_tol = 0.001)


def test_free_energy__one_mismatche():
    assert math.isclose(free_energy("GGACTGACG", "CCTGGCTGC", 310.15), -8.348, abs_tol = 0.001)
