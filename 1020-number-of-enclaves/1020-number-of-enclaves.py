from collections import deque
class Solution:
    def numEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j] == 1:
                        q.append((i, j))
                        visited[i][j] = 1
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        while q:
            i, j = q.popleft()
            for k in range(4):
                newi = i + di[k]
                newj = j + dj[k]
                if 0 <= newi < n and 0 <= newj < m and grid[newi][newj] == 1 and visited[newi][newj] == 0:
                    q.append((newi, newj))
                    visited[newi][newj] = 1
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count += 1

        return count

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        