class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            last_bit = n & 1       # get last bit
            res = (res << 1) | last_bit  # add to result
            n >>= 1               # drop last bit
        return res