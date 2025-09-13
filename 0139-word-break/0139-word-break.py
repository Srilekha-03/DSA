class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        unoset=set()
        for i in wordDict:
            unoset.add(i)

        def solve(ind,s):
            if ind>=n:
                return True
            if s in unoset:
                return True
            for l in range(1,n+1):
                temp=s[ind:ind+l]
                if temp in unoset and solve(ind+l,s):
                    return True
            return False
        return solve(0,s)
        
        