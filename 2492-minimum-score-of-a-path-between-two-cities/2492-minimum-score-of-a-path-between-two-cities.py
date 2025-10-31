from collections import defaultdict,deque
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
        q=deque()
        q.append(1)
        vis[1]=1
        while q:
            node=q.popleft()
            for val in d[node]:
                next=val[0]
                dis=val[1]
                self.max=min(self.max,dis)
                if vis[next]!=1:
                    vis[next]=1
                    q.append(next)
        return self.max
        


