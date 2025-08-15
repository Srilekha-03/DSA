from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colorr=[-1]*n

        def bfs(index,color):
            q=deque()
            q.append(index)
            colorr[index]=color
            while q:
                u=q.popleft()
                for chi in graph[u]:
                    if colorr[chi]==color:
                        return False
                    elif colorr[chi]==-1:
                        if bfs(chi,1-color)==False:
                            return False
            return True

        for i in range(n):
            if colorr[i]==-1:
                if bfs(i,0)==False:
                    return False
        return True

