class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n=len(s)
        maxi=0
        i=0
        se=set()
        se.add(s[i])
        for j in range(1,n):
            if s[j] in se:
                while s[j] in se:
                    se.remove(s[i])
                    i+=1
            se.add(s[j])
            count=j-i+1
            maxi=max(count,maxi)
        return maxi