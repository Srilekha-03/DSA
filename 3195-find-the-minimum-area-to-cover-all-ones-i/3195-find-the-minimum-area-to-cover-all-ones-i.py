class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minr, maxr = m, -1
        minc, maxc = n, -1

        for r in range(m):
            row = grid[r]
            for c in range(n):
                if row[c] == 1:
                    if r < minr: minr = r
                    if r > maxr: maxr = r
                    if c < minc: minc = c
                    if c > maxc: maxc = c

        if maxr == -1:
            return 0
        return (maxr - minr + 1) * (maxc - minc + 1)