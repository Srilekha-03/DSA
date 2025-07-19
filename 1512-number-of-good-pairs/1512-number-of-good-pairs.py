from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        d=defaultdict(int)
        for i in range(n):
            d[nums[i]]+=1
        for i in d:
            val=d[i]
            res+=(val*(val-1))//2#ncr formula which is nc2, cause we have to form a pair of 2 in the given count
        return res
            

        
        
        