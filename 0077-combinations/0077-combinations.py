class Solution:
    def combine(self, n: int, k: int):
        res = []
        c = []

        def helper(i):
            if len(c) == k:
                res.append(c.copy())
                return

            for j in range(i, n + 1):
                c.append(j)
                helper(j + 1)
                c.pop()

        helper(1)
        return res