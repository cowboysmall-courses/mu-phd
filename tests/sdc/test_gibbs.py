
import math

from sdc.gibbs import free_energy


def test_free_energy__no_mismatches():
    assert math.isclose(free_energy("CGTTGA", "GCAACT", 273.15 + 37), -5.357, abs_tol = 0.001)

def test_free_energy__one_mismatch():
    assert math.isclose(free_energy("GGACTGACG", "CCTGGCTGC", 273.15 + 37), -8.3487, abs_tol = 0.001)
