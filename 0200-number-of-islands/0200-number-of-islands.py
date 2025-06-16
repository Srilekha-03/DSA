class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        islands = 0
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0" or visited[i][j]:
                return
            visited[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    dfs(i, j)

        return islands
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        