class Solution:
    def __init__(self):
        self.dp = None

    def solve(self, s, l, r):
        if l >= r:
            return True
        if self.dp[l][r] != -1:
            return self.dp[l][r]
        if s[l] == s[r]:
            self.dp[l][r] = self.solve(s, l + 1, r - 1)
        else:
            self.dp[l][r] = False
        return self.dp[l][r]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.dp = [[-1 for _ in range(n)] for _ in range(n)]
        maxlen = 0
        startIndex = 0  
        for i in range(n):
            for j in range(i, n):
                if self.solve(s, i, j):
                    if j - i + 1 > maxlen:
                        maxlen = j - i + 1
                        startIndex = i
        return s[startIndex:startIndex + maxlen]
                    
        