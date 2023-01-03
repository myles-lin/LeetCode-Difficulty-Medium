# Runtime 1970 ms, Memory 28.6 MB
class Solution:
    def maxSubArray(self, nums: int) -> int:
        sum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            sum = max(sum + nums[i], nums[i])
            maxSum = max(sum, maxSum)
        return maxSum

# nums = [-2,1,-3,4,-1,2,1,-5,4] # Output: 6
# Solution().maxSubArray(nums)
