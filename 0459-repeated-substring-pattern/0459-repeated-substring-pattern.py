class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        #we can also try from l = n//2 to l = 1 ,for l in range(n//2, 0, -1) i.e, for easy computation for large testcases
        for l in range(1, n//2 + 1):        
            if n % l == 0:
                times = n // l              
                pattern = s[:l]
                new_str = ""
                for _ in range(times):
                    new_str += pattern               
                if new_str == s:
                    return True
        
        return False