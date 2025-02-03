class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(j-i)>k:
                    break
                if nums[i]==nums[j] and abs(j-i)<=k:
                    return True
                    break
        return False
                
                
        