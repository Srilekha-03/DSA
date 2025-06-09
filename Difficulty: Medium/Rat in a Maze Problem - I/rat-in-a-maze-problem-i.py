class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        def solve(i,j,n,m,ans,path,visited):
            if i==n-1 and j==m-1:
                ans.append(path[:])
                return
            if i+1<n and visited[i+1][j]==0 and maze[i+1][j]==1:
                visited[i][j]=1
                solve(i+1,j,n,m,ans,path+"D",visited)
                visited[i][j]=0
            if j-1>=0 and visited[i][j-1]==0 and maze[i][j-1]==1:
                visited[i][j]=1
                solve(i,j-1,n,m,ans,path+"L",visited)
                visited[i][j]=0
            if j+1<m and visited[i][j+1]==0 and maze[i][j+1]==1:
                visited[i][j]=1
                solve(i,j+1,n,m,ans,path+"R",visited)
                visited[i][j]=0
            if i-1>=0 and visited[i-1][j]==0 and maze[i-1][j]==1:
                visited[i][j]=1
                solve(i-1,j,n,m,ans,path+"U",visited)
                visited[i][j]=0
            
        n=len(maze)
        m=len(maze[0])
        ans=[]
        visited=[[0 for i in range(m)]for j in range(n)]
        if maze[0][0]==1:
            solve(0,0,n,m,ans,"",visited)
        return ans
        
        
        # code here