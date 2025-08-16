class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[0]*n
        count=0
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px=find(x)
            py=find(y)
            if px==py:
                return 
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py
            else:
                parent[px]=py
                rank[py]+=1
        for u,v in connections:
            if find(u)!=find(v):
                union(u,v)
            else:
                count+=1
        networks=len(set(find(i) for i in range(n)))
        if count>=networks-1:
            return networks-1
        return -1
        
        
            


        