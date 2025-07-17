from collections import defaultdict
class Solution:
    def canFinish(self, V: int, edges: List[List[int]]) -> bool:
        adj=defaultdict(list)
        res=[]
        queue=[]
        indegree=[0]*V
        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1
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
        return len(res)==V
        