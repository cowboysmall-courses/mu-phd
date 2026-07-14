
from typing import List

import numpy as np


def minimum_coins(coins: List[int], amount: int):
    count = len(coins)

    dp = np.zeros((count + 1, amount + 1), dtype=object)
    dp[0, 1:] = float("inf")

    for i in range(1, count + 1):
        for j in range(amount + 1):
            remainder = j - coins[i - 1]

            if remainder < 0:
                dp[i, j] = dp[i - 1, j]

            elif remainder == 0:
                dp[i, j] = 1

            else:
                dp[i, j] = min(dp[i - 1, j], 1 + dp[i, remainder])

    return dp[count, amount] if dp[count, amount] != float("inf") else -1


def print_result(coins: List[int], amount: int):
    joined = ", ".join(str(c) for c in coins)
    print(f"\t{joined:>10}\t{amount:>5}\t{minimum_coins(coins, amount):>5}")


def main() -> None:
    print("\n")
    print("\tDP: Coin Change Problem - Minimum Coins Required To Make Change\n")
    print("\n")

    print("\t     Coins\tTotal\tCount")
    print_result([1, 2, 3], 4)
    print_result([4, 6, 2], 5)
    print_result([25, 10, 5], 30)
    print_result([2, 3, 5, 6], 10)
    print_result([9, 6, 5, 1], 19)
    print("\n")
