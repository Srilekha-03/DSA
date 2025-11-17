class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        n=len(s)
        maxi=1
        i=0
        se=set()
        for j in range(n):
            while s[j] in se:
                se.remove(s[i])
                i+=1
            se.add(s[j])
            maxi=max(j-i+1,maxi)
        return maxi