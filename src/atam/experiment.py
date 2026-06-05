
from dataclasses import dataclass

import matplotlib.axis as axis
import matplotlib.pyplot as plt
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


def xor_tile(up, right) -> Tile:
    if up + right == 1:
        return Tile(1, up, 1, right, "1")
    else:
        return Tile(0, up, 0, right, "0")


def main() -> None:
    dim = 50

    tile_set = []

    for row in range(dim):
        tile_set.append([])
        for col in range(dim):
            if (row + col) == 0:
                tile_set[0].append(seed())
            elif row == 0:
                tile_set[0].append(west())
            elif col == 0:
                tile_set[row].append(north())
            elif row > 0 and col > 0:
                tile_set[row].append(xor_tile(tile_set[row - 1][col].up, tile_set[row][col - 1].left))

    for row in reversed(tile_set):
        print(" ".join(tile.colour if tile else "_" for tile in reversed(row)))


    tiles = []

    for row in range(dim):
        tiles.append([])
        for col in range(dim):
            tiles[row].append(int(tile_set[row][col].colour))

    plt.imshow([[c for c in reversed(row)] for row in reversed(tiles)], interpolation="none")
    ax = plt.gca()
    ax.set_axis_off()
    plt.show()







