class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return ""
        maxi=0
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
            if s[i]==")":
                maxi=max(maxi,count)
                count-=1
        return maxi
        