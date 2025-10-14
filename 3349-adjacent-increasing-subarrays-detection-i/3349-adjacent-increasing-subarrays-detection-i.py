class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n<2*k:
            return False
        i = 0
        while i + 2 * k <= n:
            inc1 = True
            for x in range(i + 1, i + k):
                if nums[x] <= nums[x - 1]:
                    inc1 = False
                    break
            
            inc2 = True
            for x in range(i + k + 1, i + 2 * k):
                if nums[x] <= nums[x - 1]:
                    inc2 = False
                    break

            if inc1 and inc2:
                return True
            
            i += 1
        
        return False


        