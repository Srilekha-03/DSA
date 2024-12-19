class Solution(object):
    def singleNumber(self, nums):
        h={}
        n=len(nums)
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i,k in h.items():
            if k==1:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        