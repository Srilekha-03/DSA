class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        l=[-1]*3
        for i in range(len(s)):
            l[ord(s[i]) - ord('a')]=i
            if l[0]!=-1 and l[1]!=-1 and l[2]!=-1:
                count+=min(l)+1
        return count