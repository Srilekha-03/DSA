class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        d={}
        for i in range(n):
            if nums[i] in d and abs(i-d[nums[i]])<=k:
                return True
            else:
                d[nums[i]]=i
        return False



                
                
        