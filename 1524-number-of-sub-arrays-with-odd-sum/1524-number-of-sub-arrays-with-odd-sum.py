class Solution:
    def numOfSubarrays(self, arr):
        mod = 1000000007
        even_count, odd_count = 1, 0
        total_sum = 0
        res = 0
        for x in arr:
            total_sum += x
            if total_sum % 2 == 0:
                res = (res + odd_count) % mod
                even_count += 1
            else:
                res = (res + even_count) % mod
                odd_count += 1
        return res
        