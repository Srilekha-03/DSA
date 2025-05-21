class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(n + 1):
            binary = bin(i)
            count_ones = binary.count('1')
            result.append(count_ones)
        return result
