from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d=defaultdict(list)
        vis=[-1]*n
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        return self.solve(d,source,destination,vis)
    def solve(self,g,source,destination,vis):
        if source==destination:
            return True
        vis[source]=0
        for neigh in g[source]:
            if vis[neigh]==-1 and self.solve(g,neigh,destination,vis):
                return True
        return False


        