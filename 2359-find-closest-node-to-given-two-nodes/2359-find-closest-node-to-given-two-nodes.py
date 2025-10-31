class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1==node2:
            return node1
        if edges[node1]==-1 and edges[node2]==-1:
            return -1
        n=len(edges)
        d1=[float('inf')]*n
        d2=[float('inf')]*n
        d1[node1]=0
        d2[node2]=0
        v1=[False]*n
        v2=[False]*n
        res=[0]*n
        self.dfs(node1,edges,d1,v1)
        self.dfs(node2,edges,d2,v2)
        for i in range(n):
            if d1[i]>d2[i]:
                res[i]=d1[i]
            else:
                res[i]=d2[i]
        if min(res)==float('inf'):
            return -1
        return res.index(min(res))
    def dfs(self,node,edges,d,v):
        v[node]=True
        if edges[node]!=-1:
            if v[edges[node]]==False:
                d[edges[node]]=1+d[node]
                self.dfs(edges[node],edges,d,v)


        