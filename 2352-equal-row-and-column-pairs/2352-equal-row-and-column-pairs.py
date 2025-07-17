class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        count = 0

        for r in range(n):
            for c in range(n):
                is_equal = True
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        is_equal = False
                        break
                if is_equal:
                    count += 1
        return count
