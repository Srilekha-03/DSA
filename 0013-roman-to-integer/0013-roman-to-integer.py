class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        roman_map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        res=0
        for i in range(len(s)-1):
            if roman_map[s[i]]<roman_map[s[i+1]]:
                res-=roman_map[s[i]]
            else:
                res+=roman_map[s[i]]
        res+=roman_map[s[n-1]]
        return res
        