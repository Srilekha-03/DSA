class Solution:
    def kthCharacter(self, k: int) -> str:
        shifts = bin(k - 1).count('1')
        return chr(ord('a') + shifts)
        