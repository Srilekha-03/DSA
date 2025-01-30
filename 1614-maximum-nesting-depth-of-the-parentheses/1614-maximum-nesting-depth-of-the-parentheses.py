class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return ""
        maxi=0
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                maxi=max(maxi,count)
            if s[i]==")":
                count-=1
        return maxi
        