class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n=len(maze)
        m=len(maze[0])
        vis=set()
        vis.add(tuple(entrance))
        ans=self.dfs(entrance[0],entrance[1],entrance,maze,vis,n,m)
        if ans==float('inf'):
            return -1
        return ans
    def dfs(self,i,j,entrance,maze,vis,n,m):
        if (i==0 or i==n-1 or j==0 or j==m-1) and (i,j)!=tuple(entrance):
            return 0
        l=r=t=b=float('inf')
        if 0<=j-1<m and maze[i][j-1]!="+" and (i,j-1) not in vis:
            vis.add((i,j-1))
            l=1+self.dfs(i,j-1,entrance,maze,vis,n,m)
            vis.remove((i,j-1))
        if 0<=j+1<m and maze[i][j+1]!="+" and (i,j+1) not in vis:
            vis.add((i,j+1))
            r=1+self.dfs(i,j+1,entrance,maze,vis,n,m)
            vis.remove((i,j+1))
        if 0<=i-1<n and maze[i-1][j]!="+" and (i-1,j) not in vis:
            vis.add((i-1,j))
            t=1+self.dfs(i-1,j,entrance,maze,vis,n,m)
            vis.remove((i-1,j))
        if 0<=i+1<n and maze[i+1][j]!="+" and (i+1,j) not in vis:
            vis.add((i+1,j))
            b=1+self.dfs(i+1,j,entrance,maze,vis,n,m)
            vis.remove((i+1,j))
        return min(l,r,t,b)






