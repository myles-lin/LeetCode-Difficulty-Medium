class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numMap = {}
        for val in nums:
            if val not in numMap:
                numMap[val] = 1
            else:
                numMap[val] += 1

        res = sorted(numMap, key=lambda x:numMap[x])
        return res[0]

# nums = [2,2,3,2] # Output: 3
# Solution().singleNumber(nums)
