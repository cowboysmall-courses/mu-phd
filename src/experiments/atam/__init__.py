
from typing import Callable, List
from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Tile:
    up: int
    down: int
    left: int
    right: int
    colour: int


def create_tile_grid(dim: int, func: Callable[[Tile, Tile], Tile]) -> np.ndarray:
    tiles = np.empty((dim, dim), dtype=object)

    tiles[0,  0] = Tile(2, -1, 2, -1, 4)
    tiles[1:, 0] = Tile(2,  2, 1, -1, 3)
    tiles[0, 1:] = Tile(1, -1, 2,  2, 2)

    for row in range(1, dim):
        for col in range(1, dim):
            tiles[row, col] = func(tiles[row - 1][col], tiles[row][col - 1])

    return tiles


def create_plot(values: List[List[int]], title: str, path: str) -> None:
    plt.title(title)
    plt.imshow(values, interpolation="none")
    plt.gca().set_axis_off()
    plt.savefig(path)
