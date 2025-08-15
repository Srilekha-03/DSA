from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj={}
        for i in range(len(isConnected)):
            adj[i+1]=[j+1 for j in range(len(isConnected[i])) if isConnected[i][j]==1 and i!=j]
        vis=[0]*(n+1)
        count=0
        for i in range(1,n+1):
            if vis[i]==0:
                count+=1
                self.bfs(i,adj,vis)
        return count
    def bfs(self,i,adj,vis):
        vis[i]=1
        q=deque()
        q.append(i)
        while q:
            u=q.popleft()
            for v in adj[u]:
                if vis[v]==0:
                    q.append(v)
                    vis[v]=1
        





        
        