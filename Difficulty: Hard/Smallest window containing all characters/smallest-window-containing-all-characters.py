class Solution:
    def minWindow(self, s, p):
        if len(p) > len(s):
            return ""
        
        need = {}
        for c in p:
            need[c] = need.get(c,0) + 1
        
        have = {}
        required = len(need)
        formed = 0
        
        l = 0
        res = ""
        min_len = float('inf')
        
        for r in range(len(s)):
            c = s[r]
            have[c] = have.get(c,0) + 1
            
            if c in need and have[c] == need[c]:
                formed += 1
            
            while formed == required:
                
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                
                l += 1
        
        return res
        # code here
        