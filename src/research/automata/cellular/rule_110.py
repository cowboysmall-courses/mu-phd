
import numpy as np
import matplotlib.pyplot as plt


GRID_SIZE = 250


def rule_110(vals) -> int:
    if vals[0] == 1 and vals[1] == 1 and vals[2] == 1:
        return 0
    elif vals[0] == 1 and vals[1] == 1 and vals[2] == 0:
        return 1
    elif vals[0] == 1 and vals[1] == 0 and vals[2] == 1:
        return 1
    elif vals[0] == 1 and vals[1] == 0 and vals[2] == 0:
        return 0
    elif vals[0] == 0 and vals[1] == 1 and vals[2] == 1:
        return 1
    elif vals[0] == 0 and vals[1] == 1 and vals[2] == 0:
        return 1
    elif vals[0] == 0 and vals[1] == 0 and vals[2] == 1:
        return 1
    else: # if vals[0] == 0 and vals[1] == 0 and vals[2] == 0
        return 0


def main() -> None:
    cells = np.zeros((GRID_SIZE + 1, GRID_SIZE + 1))
    cells[0, -2] = 1

    for row in range(1, GRID_SIZE + 1):
        for col in range(1, GRID_SIZE):
            cells[row, col] = rule_110(cells[row - 1, col - 1:col + 2])

    plt.title("Cellular Automata - Rule 110")
    plt.imshow(cells, interpolation = "none", cmap = "gray_r")
    plt.gca().set_axis_off()
    plt.savefig("./output/research/automata/cellular/rule_110.png")
