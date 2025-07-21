from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        Mod=10**9 + 7
        count=0
        d=defaultdict(int)
        for i in nums:
            val=i-int(str(i)[::-1])
            d[val]+=1
        for i in d:
            if d[i]!=1:
                count+=(d[i]*(d[i]-1))//2
                count=count%Mod
        return count
        

            
        