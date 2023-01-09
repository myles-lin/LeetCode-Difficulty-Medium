class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # [7, 0] [7, 1] [6, 1] [5, 0] [5, 2] [4, 4]
        people.sort(key = lambda x:(-x[0], x[1]))
        ans = []
        for i in people:
            ans.insert(i[1], i)

        return ans

# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Solution().reconstructQueue(people)
