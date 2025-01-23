class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=0
        l=0
        n=len(s)
        maxi=0
        d=dict()
        while r<n:
            if s[r] in d:
                if d[s[r]]>=l:
                    l=d[s[r]]+1
                
            length=r-l+1
            maxi=max(maxi,length)
            d[s[r]]=r
            r+=1
        return maxi

        
