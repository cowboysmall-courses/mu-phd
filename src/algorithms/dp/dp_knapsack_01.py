
from typing import List

import numpy as np


def knapsack(weights: List[int], values: List[int], capacity: int):
    count = len(weights)

    dp = np.zeros((count + 1, capacity + 1), dtype=object)

    for i in range(1, count + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i, j] = dp[i - 1, j]
            else:
                dp[i, j] = max(dp[i - 1, j], dp[i - 1, j - weights[i - 1]] + values[i - 1])

    return dp


def knapsack_items(i: int, j: int, dp, weights, values) -> List[int]:
    if i == 0:
        return []

    if dp[i, j] > dp[i - 1, j]:
        return [i - 1] + knapsack_items(i - 1, j - weights[i - 1], dp, weights, values)
    else:
        return knapsack_items(i - 1, j, dp, weights, values)


def print_result(weights: List[int], values: List[int], capacity: int):
    count = len(weights)
    dp    = knapsack(weights, values, capacity)

    print(f"\t Weights: {weights}")
    print(f"\t  Values: {values}")
    print(f"\tCapacity: {capacity}")
    print(f"\t   Value: {dp[count, capacity]}")
    print(f"\t   Items: {knapsack_items(count, capacity, dp, weights, values)}")
    print("\n")


def main() -> None:
    print("\n")
    print("\tDP: Coin Change Problem - Count Ways To Make Change\n")
    print("\n")

    print_result([4, 5, 1], [1, 2, 3], 4)
    print_result([4, 3, 2, 1], [5, 4, 3, 2], 6)
    print_result([2, 8, 4, 2, 5], [5, 3, 2, 7, 4], 10)
    print("\n")


