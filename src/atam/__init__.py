
from dataclasses import dataclass


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

