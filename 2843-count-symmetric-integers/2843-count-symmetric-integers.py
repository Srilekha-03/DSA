class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                first_half = s[:mid]
                second_half = s[mid:]
                if sum(map(int, first_half)) == sum(map(int, second_half)):
                    count += 1
        return count
        