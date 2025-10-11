from collections import defaultdict,deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        color=[-1]*(n+1)
        for i in range(1,n+1):
            if color[i]==-1:
                if not self.bfs(adj,i,color):
                    return False
        return True

    def bfs(self,adj,i,color):
        q=deque()
        q.append(i)
        color[i]=1
        while q:
            node=q.popleft()
            for i in adj[node]:
                if color[i]==color[node]:
                    return False
                if color[i]==-1:
                    q.append(i)
                    color[i]=1-color[node]
        return True

        
        