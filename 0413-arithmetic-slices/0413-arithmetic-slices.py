class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def helper(arr):
            diff=arr[1]-arr[0]
            for i in range(2,len(arr)):
                if arr[i]-arr[i-1]!=diff:
                    return False
            return True
        count=0
        for i in range(len(nums)):
            for j in range(i+2,len(nums)):
                if helper(nums[i:j+1]):
                    count+=1
        return count
        
        

        