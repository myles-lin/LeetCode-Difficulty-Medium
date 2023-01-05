class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        idx_2, idx_3, idx_5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[idx_2] * 2, dp[idx_3] * 3, dp[idx_5] * 5)
            if dp[i] == 2 * dp[idx_2]:
                idx_2 += 1
            if dp[i] == 3 * dp[idx_3]:
                idx_3 += 1
            if dp[i] == 5 * dp[idx_5]:
                idx_5 += 1
        return dp[-1]

# n = 10 # Output: 12
# Solution().nthUglyNumber(n)
