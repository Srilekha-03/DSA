class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        result = []
        for j in range(n):
            if nums[j] == key:
                start = max(j - k, 0)
                end = min(j + k, n - 1)
                #overlap checking
                if result and result[-1] >= start:
                    start = result[-1] + 1

                for i in range(start, end + 1):
                    result.append(i)

        return result
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        