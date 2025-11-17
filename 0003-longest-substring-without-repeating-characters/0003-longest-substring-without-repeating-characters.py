class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        res=0
        l,r=0,0
        n=len(s)
        while r<n:
            ch=s[r]
            while ch in se:
                se.remove(s[l])
                l+=1
            se.add(ch)
            res=max(res,r-l+1)
            r+=1
        return res
            
        