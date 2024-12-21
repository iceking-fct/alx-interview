#!/usr/bin/python3
"""Coin Change problem"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount <total>.

    Parameters:
       - coins (list): List of coin values available.
         The value of a coin will always be an int > 0.
       - total (int): The total change to give.

    Assumes:
       - There is an infinite number of coins for each denomination in the list.

    Returns:
       - 0 if total is <= 0.
       - -1 if total cannot be met by any number of coins.
       - Minimum number of coins required otherwise.
    """
    if total <= 0:
        return 0  # Handle case for total <= 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 total

    # Fill DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

