class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key in d.keys():
            if d[key]==1:
                return key


