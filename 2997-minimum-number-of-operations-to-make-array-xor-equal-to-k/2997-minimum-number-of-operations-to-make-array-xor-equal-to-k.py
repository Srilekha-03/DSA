class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=0
        for num in nums:
            xor^=num
        res=xor^k
        return res.bit_count()
        