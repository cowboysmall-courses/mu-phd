
from sdc import get_tiles


def main() -> None:
    print("SDC: Parity\n")

    bits  = "10100100"
    tiles = get_tiles(bits)
    print("\n".join(str(tile) for tile in tiles))
    print(f"Parity({bits}) = {tiles[-1].right_instruction}\n")


    bits  = "00100100"
    tiles = get_tiles(bits)
    print("\n".join(str(tile) for tile in tiles))
    print(f"Parity({bits}) = {tiles[-1].right_instruction}\n")


    bits  = "0100100"
    tiles = get_tiles(bits)
    print("\n".join(str(tile) for tile in tiles))
    print(f"Parity({bits}) = {tiles[-1].right_instruction}\n")


    bits  = "100100100"
    tiles = get_tiles(bits)
    print("\n".join(str(tile) for tile in tiles))
    print(f"Parity({bits}) = {tiles[-1].right_instruction}\n")
