from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(n):
            return sum(int(digit) for digit in str(n))
        digit_sum_map=defaultdict(list)
        max_sum=-1
        for num in nums:
            digit_sum=sum_of_digits(num)
            digit_sum_map[digit_sum].append(num)
        for digit_sum,values in digit_sum_map.items():
            if len(values)>1:
                values.sort(reverse=True)
                max_sum = max(max_sum,values[0]+values[1])
        return max_sum
        