class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[i // 2] + 1
        return result
