
from sdc.files import read_sdc_tileset
from sdc.probability import target_configuration_probability

import math


def test_target_configuration_probability__bitcopy_4pos_0():
    probability = target_configuration_probability(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json"), 273.15 + 37)
    assert math.isclose(probability, 0.019, abs_tol = 0.001)
