
from atam import north, seed, west, Tile

import numpy as np
import matplotlib.pyplot as plt



def counter_tile(up, right) -> Tile:
    if up + right == 1:
        return Tile(1, up, 0, right, "1")
    elif up + right == 2:
        return Tile(0, up, 1, right, "0")
    else:
        return Tile(0, up, 0, right, "0")


def main() -> None:
    dim = 64

    tiles = np.empty((64, 64), dtype=object)
    for row in range(dim):
        for col in range(dim):
            if (row + col) == 0:
                tiles[0, 0] = seed()
            elif row == 0:
                tiles[0, col] = west()
            elif col == 0:
                tiles[row, 0] = north()
            elif row > 0 and col > 0:
                tiles[row, col] = counter_tile(tiles[row - 1][col].up, tiles[row][col - 1].left)

    values = [[int(tile.colour) for tile in row[::-1]] for row in tiles[::-1]]

    plt.title("aTAM - Binary Counter Experiment")
    plt.imshow(values, interpolation="none")
    plt.gca().set_axis_off()
    plt.savefig("./output/atam/experiment_counter.png")
