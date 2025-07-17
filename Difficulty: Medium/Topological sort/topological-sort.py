from collections import defaultdict
class Solution:
    
    def topoSort(self, V, edges):
        def dfs(i,adj,stack,vis):
            vis[i]=1
            for j in adj[i]:
                if vis[j]!=1:
                    dfs(j,adj,stack,vis)
            stack.append(i)
            
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        vis=[0]*V
        stack=[]
        for i in range(V):
            if vis[i]==0:
                dfs(i,adj,stack,vis)
        return stack[::-1]
            
        # Code here