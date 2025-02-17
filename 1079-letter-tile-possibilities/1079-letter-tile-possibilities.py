class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(remaining_tiles, visited):
            if visited:
                self.count += 1
            
            for i in range(len(remaining_tiles)):
                if i > 0 and remaining_tiles[i] == remaining_tiles[i-1]:
                    continue
                backtrack(remaining_tiles[:i] + remaining_tiles[i+1:], True)
        tiles_sorted = sorted(tiles)
        self.count = 0
        backtrack(tiles_sorted, False)
        return self.count
        