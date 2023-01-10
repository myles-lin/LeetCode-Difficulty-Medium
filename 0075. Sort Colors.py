class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        isTobe = True
        while isTobe: # while nums[i] > nums[i+1]
            isTobe = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    isTobe = True

        # dict
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        k = 0
        for num in 0, 1, 2:
            if num in count:
                for i in range(count[num]):
                    nums[k] = num
                    k += 1

        # list
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            if count[0] > 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] > 0:
                nums[i] = 1
                count[1] -= 1
            else:
                nums[i] = 2

# nums = [2,0,2,1,1,0] # Output: [0,0,1,1,2,2]
# nums = [2,0,1] # Output: [0,1,2]
# Solution().sortColors(nums)
