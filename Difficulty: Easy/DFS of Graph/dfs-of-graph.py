class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        def dfss(start,adj,ans,vis):
            vis[start]=1
            ans.append(start)
            for i in adj[start]:
                if vis[i]==0:
                        
                    dfss(i,adj,ans,vis)
                
        vis=[0]*len(adj)
        ans=[]
        dfss(0,adj,ans,vis)
        return ans
        