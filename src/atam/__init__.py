
from typing import Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class Tile:
    up: int
    down: int
    left: int
    right: int
    colour: str


def seed() -> Tile:
    return Tile(2, -1, 2, -1, "3")

def north() -> Tile:
    return Tile(2, 2, 1, -1, "2")

def west() -> Tile:
    return Tile(1, -1, 2, 2, "2")


def create_tile_grid(dim: int, func: Callable[[int, int], Tile]) -> np.ndarray:
    tiles = np.empty((dim, dim), dtype=object)

    for row in range(dim):
        for col in range(dim):
            if row + col == 0:
                tiles[0, 0] = seed()
            elif row == 0:
                tiles[0, col] = west()
            elif col == 0:
                tiles[row, 0] = north()
            else:
                tiles[row, col] = func(tiles[row - 1][col].up, tiles[row][col - 1].left)

    return tiles
