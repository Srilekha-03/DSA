class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count=0
        for i in range(len(s)):
            if s[i]==')':
                count-=1
            if count!=0:
                ans+=s[i]
            if s[i]=='(':
                count+=1
        return ans

        