def change(amount, length, coins, cache):
    if amount == 0: return 1
    if length == 0: return 0

    key = amount, length
    if key in cache:
        return cache[key]

    result = change(amount, length-1, coins, cache)

    if amount - coins[length-1] >= 0:
        result += change(amount - coins[length-1], length, coins, cache)

    cache[key] = result
    return result

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return change(amount, len(coins), coins, {})
        
# change(5, [1,2]) == change(5, [1]) + change(5-2, [1,2])
# change(amount, coins) == change(amount, coins[:-1]) + change(amount-coins[-1], coins)

# amount, coins = 5, [1,2,5] # Output: 4
# amount, coins = 3, [2] # Output: 0
# amount, coins = 10, [10] # Output: 1
# Solution().change(amount, coins)
