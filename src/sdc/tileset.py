

from sdc.layer import Layer
# from sdc.tile import Tile, NullTile

from typing import Dict, List


class TileSet:

    def __init__(self, layers: List[Layer]):
        self.layers = layers



