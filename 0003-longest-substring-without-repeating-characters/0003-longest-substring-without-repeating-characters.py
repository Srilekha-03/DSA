class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=dict()
        res=0
        l,r=0,0
        n=len(s)
        while r<n:
            ch=s[r]
            if ch in d and d[ch]>=l:
                l=d[ch]+1
            d[ch]=r
            res=max(res,r-l+1)
            r+=1
        return res
            
        