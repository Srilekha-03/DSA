class Solution(object):
    def minZeroArray(self, nums, queries):
        n = len(nums)
        sum_value = 0
        query_count = 0
        diff_array = [0] * (n + 1)
        for i in range(n):
            while sum_value + diff_array[i] < nums[i]:
                query_count += 1
                if query_count > len(queries):
                    return -1
                left, right, value = queries[query_count - 1]
                if right >= i:
                    diff_array[max(left, i)] += value
                    if right + 1 < len(diff_array):
                        diff_array[right + 1] -= value
            sum_value += diff_array[i]
        return query_count