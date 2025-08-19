class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        M = 10**9 + 7
        n = len(nums)
        last_index = {}
        for i in range(n):
            last_index[nums[i]] = i

        i = 0
        j = last_index[nums[0]]

        result = 1
        while i < n:
            if i > j:
                result = (result * 2) % M

            j = max(j, last_index[nums[i]])
            i += 1
        return result
        