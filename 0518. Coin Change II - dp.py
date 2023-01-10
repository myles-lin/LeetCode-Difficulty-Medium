class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]

# dp[0][0] = 1
# dp[0][i] = 0 , 1 <= i <= amount
# dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]

# amount, coins = 5, [1,2,5] # Output: 4
# amount, coins = 3, [2] # Output: 0
# amount, coins = 10, [10] # Output: 1
# Solution().change(amount, coins)
