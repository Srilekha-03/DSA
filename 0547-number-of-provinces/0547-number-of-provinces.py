class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        vis=[0]*(n+1)
        count=0
        def dfs(i):
            vis[i]=1
            ngb=isConnected[i-1]
            for j in range(1,n+1):
                if ngb[j-1]==1 and vis[j]==0:
                    dfs(j)
        for i in range(1,n+1):
            if vis[i]==0:
                count+=1
                dfs(i)
        return count
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        