class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dictMap = {}
        for val in nums:
            if val not in dictMap:
                dictMap[val] = 1
            else:
                del dictMap[val]

        return dictMap.keys()

# nums = [1,2,1,3,2,5] # Output: [3,5]
# nums = [-1,0] # Output: [-1,0]
# Solution().singleNumber(nums)
