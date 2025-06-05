from collections import defaultdict
class Solution:
    def DFS(self, adj, curr, visited):
        visited[ord(curr) - ord('a')] = 1       
        min_char = curr
        
        for v in adj[curr]:
            if visited[ord(v) - ord('a')] == 0:
                min_char = min(min_char, self.DFS(adj, v, visited))       
        return min_char
    
    def smallestEquivalentString(self, s1, s2, baseStr):
        n = len(s1)
        adj = defaultdict(list)      
        #adjacency list
        for i in range(n):
            u = s1[i]
            v = s2[i]           
            adj[u].append(v)
            adj[v].append(u) 

        m = len(baseStr)
        result = ""     
        # For each character in baseStr again finding the smallest equivalent character
        for i in range(m):
            ch = baseStr[i]   
            visited = [0] * 26           
            result += self.DFS(adj, ch, visited)
        
        return result