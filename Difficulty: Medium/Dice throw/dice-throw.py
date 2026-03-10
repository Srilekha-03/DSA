class Solution:
    def noOfWays(self, m,n,x):
        d = {}
        M = 10**9 + 7

        def solve(n, x):
            if x < 0:
                return 0

            if (n, x) in d:
                return d[(n, x)]

            if n == 0:
                return 1 if x == 0 else 0

            ways = 0
            for face in range(1, m+1):
                ways = (ways + solve(n-1, x-face)) % M

            d[(n, x)] = ways
            return ways

        return solve(n, x)
        # code here