class Solution:
    def clearDigits(self, s: str) -> str:
        st=""
        for i in range(len(s)):
            if s[i].isdigit():
                st=st[:-1]
            else:
                st+=s[i]
        return st
        