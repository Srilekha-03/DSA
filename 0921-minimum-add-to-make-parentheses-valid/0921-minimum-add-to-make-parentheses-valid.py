class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0  
        missing= 0  
        for ch in s:
            if ch == '(':
                open_count += 1  
            elif ch == ')':
                if open_count > 0:
                    open_count -= 1  
                else:
                    missing+= 1  
        return open_count + missing

        