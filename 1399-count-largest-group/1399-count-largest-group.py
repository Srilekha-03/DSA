from collections import defaultdict
class Solution:
    def findDigitsSum(self, num):
        total = 0
        while num:
            total += num % 10
            num //= 10
        return total

    def countLargestGroup(self, n):
        digit_sum_count = defaultdict(int)
        max_size = 0
        count = 0
        for num in range(1, n + 1):
            digits_sum = self.findDigitsSum(num)
            digit_sum_count[digits_sum] += 1

            if digit_sum_count[digits_sum] == max_size:
                count += 1
            elif digit_sum_count[digits_sum] > max_size:
                max_size = digit_sum_count[digits_sum]
                count = 1

        return count
