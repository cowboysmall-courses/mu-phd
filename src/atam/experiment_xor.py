
from atam import Tile, create_tile_grid

import matplotlib.pyplot as plt


def xor_tile(up: int, right: int) -> Tile:
    if up + right == 1:
        return Tile(1, up, 1, right, "1")
    else:
        return Tile(0, up, 0, right, "0")


def main() -> None:
    dim = 64

    values = [[int(tile.colour) for tile in row[::-1]] for row in create_tile_grid(dim, xor_tile)[::-1]]

    plt.title("aTAM - XOR")
    plt.imshow(values, interpolation="none")
    plt.gca().set_axis_off()
    plt.savefig("./output/atam/experiment_xor.png")
