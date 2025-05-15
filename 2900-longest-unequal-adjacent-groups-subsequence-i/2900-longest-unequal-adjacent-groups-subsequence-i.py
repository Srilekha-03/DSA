class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        l=[]
        n=len(words)
        for i in range(n):
            if i==0 or groups[i]!=groups[i-1]:
                l.append(words[i])
        return l
        