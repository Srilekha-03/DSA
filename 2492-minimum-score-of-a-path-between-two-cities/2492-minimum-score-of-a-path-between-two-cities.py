from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)
        for val in roads:
            u=val[0]
            v=val[1]
            l=val[2]
            d[u].append((v, l))
            d[v].append((u, l))
        vis=[0]*(n+1)
        self.max=float('inf')
        self.dfs(1,vis,roads,d)
        return self.max
    def dfs(self,u,vis,roads,d):
        vis[u]=1
        for i in d[u]:
            v=i[0]
            l=i[1]
            self.max=min(self.max,l)
            if vis[i[0]]==0:
                self.dfs(v,vis,roads,d)


