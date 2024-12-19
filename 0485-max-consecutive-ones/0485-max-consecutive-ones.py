class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        c=0
        for i in nums:
            if i==1:
                c+=1
                maxi=max(maxi,c)
            else:
                c=0
        return maxi
        
        """
        :type nums: List[int]
        :rtype: int
        """
        