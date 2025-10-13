class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        result = []

        for r in range(rows):
            for c in range(cols):
                reaches_pacific = [False]
                reaches_atlantic = [False]
                visited = set()
                
                self.dfs(r, c, heights, visited, reaches_pacific, reaches_atlantic)
                
                if reaches_pacific[0] and reaches_atlantic[0]:
                    result.append([r, c])
                    
        return result

    def dfs(self,r, c, heights, visited, reaches_pacific, reaches_atlantic):
        if (r, c) in visited:
            return

        visited.add((r, c))
        
        rows, cols = len(heights), len(heights[0])
        
        if r == 0 or c == 0:
            reaches_pacific[0] = True
        if r == rows - 1 or c == cols - 1:
            reaches_atlantic[0] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if heights[nr][nc] <= heights[r][c]:
                    self.dfs(nr, nc, heights, visited, reaches_pacific, reaches_atlantic)

            