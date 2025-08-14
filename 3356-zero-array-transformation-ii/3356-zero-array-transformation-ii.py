class Solution(object):
    def minZeroArray(self, nums, queries):
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0

        def can_zero(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v

            curr = 0
            for i in range(n):
                curr += diff[i]
                if nums[i] > curr:
                    return False
            return True

        lo, hi = 0, len(queries)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_zero(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
        