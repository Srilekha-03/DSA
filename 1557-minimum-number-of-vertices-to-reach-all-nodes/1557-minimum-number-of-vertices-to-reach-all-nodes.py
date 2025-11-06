class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        
        for u, v in edges:
            indegree[v] += 1
        
        result = [i for i in range(n) if indegree[i] == 0]
        return result
