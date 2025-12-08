class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                s = i*i + j*j
                k = int(s**0.5)
                if k * k == s:
                    if 1 <= k <= n:
                        ans += 1
        return ans
        