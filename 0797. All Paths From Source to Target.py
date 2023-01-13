class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path, i, graph, result):
            if i == len(graph) - 1:
                result.append(path)

            for j in graph[i]:
                newPath = path + [j]
                dfs(newPath, j, graph, result)
                
        result = []
        dfs([0], 0, graph, result)
        return result

# graph = [[1,2],[3],[3],[]] # Output: [[0,1,3],[0,2,3]]
# graph = [[4,3,1],[3,2,4],[3],[4],[]] # Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# Solution().allPathsSourceTarget(graph)
