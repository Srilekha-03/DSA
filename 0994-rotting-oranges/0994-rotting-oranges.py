from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        q = deque()
        cnt_fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j)) 
                    vis[i][j] = 2
                elif grid[i][j] == 1:
                    cnt_fresh += 1
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]  
        level=0     
        cnt = 0    
        while q:
            size=len(q)
            for g in range(size):
                r, c= q.popleft()
                for i in range(4):
                    nrow = r + drow[i]
                    ncol = c + dcol[i]
                    if 0 <= nrow < n and 0 <= ncol < m:
                        if vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                            q.append((nrow, ncol))
                            vis[nrow][ncol] = 2
                            cnt += 1
            level+=1       
        if cnt != cnt_fresh:
            return -1        
        return level-1
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        