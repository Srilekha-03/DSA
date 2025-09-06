from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        res=0
        for i in range(n):
            freq=Counter()
            for j in range(i,n):
                freq[s[j]]+=1
                ans = list(freq.values())
                res += max(ans) - min(ans)      
        return res

        