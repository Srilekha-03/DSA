class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        d1 = set()
        d2 = set()
        
        def backtrack(r):
            if r == n:
                return 1
            
            count = 0
            
            for c in range(n):
                if c in cols or (r-c) in d1 or (r+c) in d2:
                    continue
                
                cols.add(c)
                d1.add(r-c)
                d2.add(r+c)
                
                count += backtrack(r+1)
                
                cols.remove(c)
                d1.remove(r-c)
                d2.remove(r+c)
            
            return count
        
        return backtrack(0)