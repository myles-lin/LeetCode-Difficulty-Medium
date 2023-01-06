def diff(c):
    return c[0] - c[1]

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=diff)
        teamA = 0
        ans = 0 
        for costA, costB in costs:
            if teamA < len(costs) // 2:
                ans += costA
                teamA += 1
            else:
                ans += costB
        return ans

# costs = [[10,20],[30,200],[400,50],[30,20]] # Output: 110
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]] # Output: 1859
# costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]] # Output: 3086
# Solution().twoCitySchedCost(costs)
