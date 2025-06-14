class Solution(object):
    def solve(self, board):
        n=len(board)
        m=len(board[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        rowi=[-1,0,+1,0]
        coli=[0,+1,0,-1]
        def dfs(row,col):
            vis[row][col]=1
            for i in range(4):
                newrow=row+rowi[i]
                newcol=col+coli[i]
                if 0<=newrow<n and 0<=newcol<m and vis[newrow][newcol]==0 and board[newrow][newcol] == "O":
                    dfs(newrow,newcol)
        #for rows
        for i in range(m):
            if vis[0][i]==0 and board[0][i]=="O":
                dfs(0,i)
            if vis[n-1][i]==0 and board[n-1][i]=="O":
                dfs(n-1,i)
        #for cols
        for i in range(n):
            if vis[i][0]==0 and board[i][0]=="O":
                dfs(i,0)
            if vis[i][m-1]==0 and board[i][m-1]=="O":
                dfs(i,m-1)
        
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and board[i][j]=="O":
                    board[i][j]="X"





        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        