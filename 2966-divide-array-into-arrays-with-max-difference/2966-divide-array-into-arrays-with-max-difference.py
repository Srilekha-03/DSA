class Solution(object):
    def divideArray(self, nums, k):
        ans=[]
        nums.sort()
        for i in range(0,len(nums),3):
            triplet=nums[i:i+3]
            if triplet[2]-triplet[0]>k:
                return []
            ans.append(triplet)
        return ans


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        