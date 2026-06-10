
from atam import Tile, create_tile_grid, create_plot


def xor_tile(below: Tile, before: Tile) -> Tile:
    if below.up + before.left == 1:
        return Tile(1, below.up, 1, before.left, 1)
    else:
        return Tile(0, below.up, 0, before.left, 0)


def main() -> None:
    dim    = 64
    tiles  = create_tile_grid(dim, xor_tile)
    values = [[tile.value for tile in row[::-1]] for row in tiles[::-1]]

    create_plot(values, "aTAM - XOR", "./output/atam/experiment_xor.png")
