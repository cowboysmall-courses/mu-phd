
from typing import List

import numpy as np


def count_ways(coins: List[int], total: int):
    count = len(coins)

    dp = np.zeros((count + 1, total + 1), dtype=object)
    dp[0, 0] = 1

    for i in range(1, count + 1):
        for j in range(total + 1):
            remainder = j - coins[i - 1]

            if remainder >= 0:
                dp[i, j] += dp[i, remainder]

            dp[i, j] += dp[i - 1, j]

    return dp[count, total]


def print_result(coins: List[int], total: int):
    joined = ", ".join(str(c) for c in coins)
    print(f"\t{joined:>10}\t{total:>5}\t{count_ways(coins, total):>4}")


def main() -> None:
    print("\n")
    print("\tDP: Coin Change Problem - Count Ways To Make Change\n")
    print("\n")

    print("\t     Coins\tTotal\tWays")
    print_result([1, 2, 3], 4)
    print_result([4, 6, 2], 5)
    print_result([25, 10, 5], 30)
    print_result([2, 3, 5, 6], 10)
    print_result([9, 6, 5, 1], 19)
    print("\n")
