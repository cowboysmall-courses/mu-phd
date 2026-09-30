
import math

from utils.gibbs import free_energy


def test_free_energy():
    assert math.isclose(free_energy("CGTTGA", "GCAACT", 310.15), -5.357, abs_tol = 0.001)
