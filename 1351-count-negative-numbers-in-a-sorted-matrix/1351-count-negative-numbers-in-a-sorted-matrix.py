class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for val in row:
                if val < 0:
                    count += 1
        return count