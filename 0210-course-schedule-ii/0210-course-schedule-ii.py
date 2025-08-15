from collections import defaultdict
class Solution:
    def findOrder(self, V: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        res=[]
        queue=[]
        indegree=[0]*V
        for u,v in edges:
            adj[v].append(u)
            indegree[u]+=1
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node=queue.pop(0)
            res.append(node)
            for j in adj[node]:
                indegree[j]-=1
                if indegree[j]==0:
                    queue.append(j)
        if len(res)==V:
            return res
        else:
            return []
        