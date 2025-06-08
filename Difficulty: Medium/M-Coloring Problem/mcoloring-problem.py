# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        
        adj = [[] for _ in range(v)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u) 
        color = [0] * v  
        def isSafe(node, c):
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    return False
            return True

        def solve(node):
            if node == v:
                return True 

            for c in range(1, m + 1):
                if isSafe(node, c):
                    color[node] = c
                    if solve(node + 1):
                        return True
                    color[node] = 0
            return False

        return solve(0)
