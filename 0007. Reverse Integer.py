# Runtime 55 ms, Memory 13.9 MB
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = -1 * int(str(-x)[::-1])

        if ans > 2**31 -1 or ans < -2**31:
            ans = 0
        return ans

# x = 123 # Output: 321
# x = -321 # Output: -321
# x = 120 # Output: 21
# Solution().reverse(x)
