"""

    Notes:

    For further research some or all of the following need to be taken into consideration:

    1) If left unattended, the temperature in the container falls according to Newton's Law of Cooling
    2) The state of the system is dictated by energy / temperature according to the Boltzman distribution



"""


from dataclasses import dataclass

import random


@dataclass
class Tile:
    left_instruction: int
    right_instruction: int
    left_input: str
    right_input: str
    position: int
    value: int = 0
    # seed: float = random.random()


def has_left(scaffold, index) -> bool:
    return 0 < index and (index - 1) in scaffold and scaffold[index - 1] is not None

def has_right(scaffold, index) -> bool:
    return index < 3 and (index + 1) in scaffold and scaffold[index + 1] is not None

def check_left(scaffold, index, tile) -> bool:
    return (scaffold[index - 1].right_instruction != scaffold[index].left_instruction) and (scaffold[index - 1].right_instruction == tile.left_instruction)

def check_right(scaffold, index, tile) -> bool:
    return (scaffold[index].right_instruction != scaffold[index + 1].left_instruction) and (tile.right_instruction != scaffold[index + 1].left_instruction)



def main() -> None:
    print("\n")
    print("\tA Simulation of Scaffolded DNA Computer: Parity")
    print("\n")

    # Step 1: create a fixed number of tiles of each type, for each scaffold position
    tiles = [
        Tile(0, 1, "10", "01", 1, 1),
        Tile(1, 0, "10", "01", 1, 0),
        Tile(0, 1, "01", "00", 2, 1),
        Tile(1, 0, "01", "00", 2, 0),
        Tile(1, 1, "00", "--", 3, 1),
        Tile(0, 0, "00", "--", 3, 0)
    ] * 1000
    random.shuffle(tiles)


    # Step 2: create a fixed number of scaffolds for the operation, with anchor tiles
    scaffolds = [
        {
            0: Tile(0, 1, "10", "10", 0, 1)
        }
    ] * 10

    # Step 3: run the simulation for each scaffold for each position
    #    - for each scaffold randomly pick a tile from the solution
    #    - if the tile is for a vacant position, place it and proceed
    #    - if the tile is for a taken position,
    #      and the existing tile is imperfectly bound,
    #      (and the tile binds more perfectly with the surrounding tiles)
    #      then replace according to a probability (perhaps influenced by temp)
    #    - otherwise continue from the beginning with the next scaffold
    #    - continue until experiment concludes
    #    - collect completed scaffolds, both correct and incorrect
    #    - report on the outcome

    # placed = []

    for i in range(100):
        for scaffold in scaffolds:
            tile = tiles.pop()
            index = tile.position

            if index not in scaffold:

                scaffold[index] = tile

            elif (has_left(scaffold, index) and check_left(scaffold, index, tile)) or (has_right(scaffold, index) and check_right(scaffold, index, tile)):

                threshold = 0.75
                if has_left(scaffold, index) and check_left(scaffold, index, tile):
                    threshold -= 0.25
                if has_right(scaffold, index) and check_right(scaffold, index, tile):
                    threshold -= 0.25

                rand = random.random()

                if rand > threshold:
                    tiles.append(scaffold[index])
                    scaffold[index] = tile

            else:
                tiles.append(tile)

    # count = 0
    # for scaffold in scaffolds:
    #     if 3 in scaffold:
    #         count += scaffold[3].value

    # print(f"Completed Correctly: {count}")
    # print()

    for scaffold in scaffolds:
        print(scaffold)
        # for i in range(4):
        #     print(f"Index {i} -> {scaffold[i]}")
        print()
    print()

