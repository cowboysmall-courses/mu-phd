
from experiments.atam import Tile, create_tile_grid, create_plot


def counter_tile(below: Tile, before: Tile) -> Tile:
    if below.up + before.left == 1:
        return Tile(1, below.up, 0, before.left, 1)
    elif below.up + before.left == 2:
        return Tile(0, below.up, 1, before.left, 0)
    else:
        return Tile(0, below.up, 0, before.left, 0)


def main() -> None:
    tiles  = create_tile_grid(64, counter_tile)
    values = [[tile.colour for tile in row[::-1]] for row in tiles[::-1]]

    create_plot(values, "aTAM - Counter", "./output/atam/experiment_counter.png")
