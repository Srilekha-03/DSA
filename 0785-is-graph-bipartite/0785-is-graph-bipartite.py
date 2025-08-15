class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colorr=[-1]*n

        def dfs(index,color):
            colorr[index]=color
            for chi in graph[index]:
                if colorr[chi]==color:
                    return False
                elif colorr[chi]==-1:
                    if dfs(chi,1-color)==False:
                        return False
            return True

        for i in range(n):
            if colorr[i]==-1:
                if dfs(i,0)==False:
                    return False
        return True

        



        