from collections import defaultdict
class Solution:
    def findOrder(self, V: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        vis=[0]*V
        inRecur=[0]*V
        res=[]
        for u,v in edges:
            adj[u].append(v)
        for i in range(V):
            if vis[i]==0 and self.dfs(adj,vis,inRecur,i,res):
                return []
        return res
    def dfs(self,adj,vis,inRecur,i,res):
        vis[i]=1
        inRecur[i]=1
        for j in adj[i]:
            if vis[j]==0:
                if self.dfs(adj, vis, inRecur, j,res):
                    return True
            elif inRecur[j]==1:
                return True  
        res.append(i)              
        inRecur[i]=0
        return False
        