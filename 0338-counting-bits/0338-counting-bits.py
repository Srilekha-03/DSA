class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(n + 1):
            count_ones =bin(i).count('1')
            result.append(count_ones)
        return result
