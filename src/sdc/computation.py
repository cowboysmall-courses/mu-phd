
from sdc.layer import Layer
from sdc.scaffold import Scaffold
from sdc.tile import Tile, NullTile

from typing import Dict, List


class Computation:

    def __init__(self, scaffold: Scaffold, layers: List[List[Tile]]):
        self.scaffold = scaffold
        self.layers = layers

