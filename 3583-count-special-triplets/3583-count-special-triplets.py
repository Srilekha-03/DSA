from collections import defaultdict
class Solution(object):
    def specialTriplets(self, nums):
        freqLeft=defaultdict(int)
        freqRight=defaultdict(int)
        triplets=0
        MOD = 10**9 + 7
        for num in nums:
            freqRight[num]+=1
        for i in range(len(nums)):
            num=nums[i]
            freqRight[num]-=1
            double=num*2
            triplets+=freqLeft[double]*freqRight[double]
            triplets=triplets%MOD
            freqLeft[num]+=1
        return triplets
            
        """
        :type nums: List[int]
        :rtype: int
        """
        