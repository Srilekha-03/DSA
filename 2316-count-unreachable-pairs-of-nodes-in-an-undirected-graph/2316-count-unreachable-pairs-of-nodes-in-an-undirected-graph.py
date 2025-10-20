from collections import Counter
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
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
        for u,v in edges:
            if find(u)!=find(v):
                union(u,v)
        comp_sizes=Counter(find(i) for i in range(n))
        ans=0
        remaining=n
        for key,val in comp_sizes.items():
            size=val
            ans+=size*(remaining-size)
            remaining=remaining-size
        return ans


