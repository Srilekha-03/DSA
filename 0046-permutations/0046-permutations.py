class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        p = []
        used = set()
        n = len(nums)
        def helper():
            if len(p) == n:
                res.append(p.copy())
                return

            for i in range(n):
                if i not in used:
                    p.append(nums[i])
                    used.add(i)
                    helper()
                    p.pop()
                    used.remove(i)

        helper()
        return res