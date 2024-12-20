class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
        #step 1 finding out the break point
        index=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            nums[0:n] = list(reversed(nums[0:n]))
            return nums
        #step 2 finding the next greater ele to swap it with
        for i in range(n-1,index,-1):
            if nums[i]>nums[index]:
                nums[i],nums[index]=nums[index],nums[i]
                break
        #step 3 reversing the rest ele after swapping from index + 1
        nums[index+1:n]=list(reversed(nums[index+1:n]))
        return nums
        

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        