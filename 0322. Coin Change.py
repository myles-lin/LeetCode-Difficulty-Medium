class Solution:
    def coinChange(self, coins: int, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                if dp[i - c] != float('inf'):
                    dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

# coins, amount = [1,2,5], 11 # Output: 3
# Solution().coinChange(coins, amount)
