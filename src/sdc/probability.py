
from sdc.mfe import minimum_free_energy
from sdc.pf import partition_function
from sdc.tile import Tile
from sdc import R_j

from typing import List

import math


def target_configuration_probability(tiles: List[List[Tile]], T: float) -> float:
    return math.exp( -(minimum_free_energy(tiles, T)) / (R_j * T) ) / partition_function(tiles, T)
