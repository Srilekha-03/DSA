class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        result=[]
        for i in range(n):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        for i in range(n):
            if nums[i]>0:
                result.append(i+1)
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        