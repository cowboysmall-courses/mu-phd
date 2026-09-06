
from experiments.sdc import Tile


ANCHOR = Tile(0, 1, "1", "1", 0, 1)

TILES = [
    Tile(1, 1, "1", "1", 1, 1),
    Tile(0, 0, "0", "0", 1, 0),
    Tile(1, 1, "1", "1", 2, 1),
    Tile(0, 0, "0", "0", 2, 0),
    Tile(1, 1, "1", "1", 3, 1),
    Tile(0, 0, "0", "0", 3, 0)
]

SOLUTION = [
    Tile(0, 1, "1", "1", 0, 1),
    Tile(1, 1, "1", "1", 1, 1),
    Tile(1, 1, "1", "1", 2, 1),
    Tile(1, 1, "1", "1", 3, 1)
]
