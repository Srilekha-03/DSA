class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]* (n+1)
        for i in range(1,n + 1):
            result[i]=(i).bit_count()
        return result
            
