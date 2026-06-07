
from atam import Tile, create_tile_grid

import matplotlib.pyplot as plt


def counter_tile(up: int, right: int) -> Tile:
    if up + right == 1:
        return Tile(1, up, 0, right, "1")
    elif up + right == 2:
        return Tile(0, up, 1, right, "0")
    else:
        return Tile(0, up, 0, right, "0")


def main() -> None:
    dim = 65

    values = [[int(tile.colour) for tile in row[::-1]] for row in create_tile_grid(dim, counter_tile)[::-1]]

    plt.title("aTAM - Binary Counter")
    plt.imshow(values, interpolation="none")
    plt.gca().set_axis_off()
    plt.savefig("./output/atam/experiment_counter.png")
