class Solution(object):
    def missingNumber(self, arr):
        n=len(arr)
        xor1=0
        xor2=0
        for i in range(n):
            xor1=xor1^arr[i]
            xor2=xor2^i
        xor2=xor2^n
        return xor1^xor2
        """
        :type nums: List[int]
        :rtype: int
        """
        