class Solution:
	def isCycle(self, V, edges):
	    adj=[[]for i in range(V)]
	        
	    for u,v in edges:
	        adj[u].append(v)
	        adj[v].append(u)
	    vis=[0]*V
	        
	    def detectloop(i):
	        vis[i]=1
	        q=[]
	        q.append([i,-1])
	        while q:
	            node,parent=q.pop(0)
	            for ngb in adj[node]:
	                if vis[ngb]==0:
	                    vis[ngb]=1
	                    q.append([ngb,node])
	                elif vis[ngb]==1 and  ngb!=parent:
	                    return True
	        return False
	    
        for i in range(len(vis)):
            if vis[i]==0:
                if detectloop(i):
                    return True
        return False
	   
	               
	   
		#Code here