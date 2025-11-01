class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        vis=[[0 for i in range(m)]for i in range(n)]

        def dfs(i,j,k,vis,word):
            vis[i][j]=1
            if k==len(word):
                return True
            dir=[(0,-1),(1,0),(0,1),(-1,0)]
            for g in range(4):
                new_i=i+dir[g][0]
                new_j=j+dir[g][1]
                if 0<=new_i<n and 0<=new_j<m and vis[new_i][new_j]==0 and board[new_i][new_j]==word[k]:
                    if dfs(new_i,new_j,k+1,vis,word):
                        return True
            vis[i][j]=0
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if dfs(i,j,1,vis,word):
                        return True
        return False

        