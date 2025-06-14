from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        n=len(mat)
        m=len(mat[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        dis=[[0 for i in range(m)]for j in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    vis[i][j]=1
        rowi=[-1,0,+1,0]
        coli=[0,+1,0,-1]
        while q:
            row,col,step=q.popleft()
            dis[row][col]=step
            for i in range(4):
                newrow=row+rowi[i]
                newcol=col+coli[i]
                if 0<=newrow<n and 0<=newcol<m and vis[newrow][newcol]==0:
                    q.append([newrow,newcol,step+1])
                    vis[newrow][newcol]=1

        return dis


        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        