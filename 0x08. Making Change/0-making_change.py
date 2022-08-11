#!/usr/bin/python3

def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given smount

    Args:
        coins (List): a list of coins available
        total (sum): the total sum needed to complete target
    """

    dp = [total+1]*(total+1)
        
    dp[0] = 0
    for a in range(total+1):
        for c in coins:
          if a-c>=0:
            dp[a]=min(dp[a],1+dp[a-c])
    return dp[total] if dp[total]!=total+1 else -1
