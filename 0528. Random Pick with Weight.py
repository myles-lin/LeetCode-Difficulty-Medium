class Solution:
    def __init__(self, w: List[int]):
        self.__w = w
        a = [None] * len(w)
        a[0] = w[0]
        for i in range(1, len(w)):
            a[i] = a[i-1] + w[i]
        self.__a = a
        # self.__a = [1, 4, 7]
    
    def pickIndex(self) -> int:
        d = random.randrange(self.__a[-1])
        # 較沒有效率
        # for i, val in enumerate(self.__a):
        #     if d < val:
        #         return i

        # (Binary search)
        left, right = 0, len(self.__a) # l: 0, r:3
        while left < right:
            mid = (left + right) // 2
            if d < self.__a[mid]:
                if mid == 0 or d >= self.__a[mid-1]:
                    return mid
                right = mid
            else:
                left = mid + 1

# w = [1, 3, 3]
# obj = Solution(w)
# obj.pickIndex()
