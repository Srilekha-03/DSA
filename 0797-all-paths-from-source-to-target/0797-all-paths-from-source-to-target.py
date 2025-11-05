class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res=[]
        n=len(graph)
        path=[]
        vis=[False]*n
        self.dfs(0,n-1,path,vis,graph)
        return self.res
    def dfs(self,source,dest,path,vis,graph):
        vis[source]=True
        path.append(source)
        if source==dest:
            self.res.append(path[:])
            vis[source]=False
            path.pop()
            return
        for neigh in graph[source]:
            if not vis[neigh]:
                self.dfs(neigh,dest,path,vis,graph)
        path.pop()
        vis[source]=False
        