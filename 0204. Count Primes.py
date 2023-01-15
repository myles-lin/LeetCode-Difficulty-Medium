class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isPrimes = [True] * n
        isPrimes[0] = False
        isPrimes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if isPrimes[i]:
                for j in range(i*2, n, i):
                    isPrimes[j] = False

        return sum(isPrimes)

# n = 10 # Output: 4
# Solution().countPrimes(n)
