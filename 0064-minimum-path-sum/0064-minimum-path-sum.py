class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        t = [[-1] * n for _ in range(m)]

        def MPS(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if t[i][j] != -1:
                return t[i][j]

            if i == m - 1:
                t[i][j] = grid[i][j] + MPS(i, j + 1)
            elif j == n - 1:
                t[i][j] = grid[i][j] + MPS(i + 1, j)
            else:
                t[i][j] = grid[i][j] + min(MPS(i + 1, j), MPS(i, j + 1))
            return t[i][j]

        return MPS(0, 0)


        