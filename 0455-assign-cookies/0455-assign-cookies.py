class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l=0
        r=0
        n=len(g)
        m=len(s)
        while l<n and r<m:
            if g[l]<=s[r]:
                l+=1
            r+=1
        return l
        
        