#!/usr/bin/python3
"""Coin Change problem"""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to
    meet a given amount <total>.

    Params:
       - coins(obj:list): a list of coin values available.
         The value of a coin will always be an int > 0
       - total(number): the total change to give.

    Assumes:
       - There is an infinite number of coins for each denomination
         in our list.
    Returns:
       - 0 if total is <= 0
       - -1 if total cannot be met by any number of coins we have
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize DP table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

