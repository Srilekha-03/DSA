class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0        
        for i in range(32):
            bit = 1 << i
            countOne = 0            
            for num in nums:
                if num & bit:
                    countOne += 1          
            if countOne % 3:
                result |= bit
        # Handling negative numbers
        if result >= 2**31:
            result -= 2**32

        return result

        