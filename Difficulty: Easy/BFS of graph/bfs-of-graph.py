class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n=len(adj)
        vis=[0]*n
        q=[]
        q.append(0)
        vis[0]=1
        ans=[]
        while q:
            node=q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if vis[i]==0:
                    q.append(i)
                    vis[i]=1
        return ans
                    
        # code here