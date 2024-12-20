class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        nums1=[0]*n
        pos=0
        neg=1
        for i in range(n):
            if nums[i]<0:
                nums1[neg]=nums[i]
                neg+=2
            else:
                nums1[pos]=nums[i]
                pos+=2
        return nums1

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        