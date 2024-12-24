class Solution(object):
    def splitArray(self, nums, k):
        n=len(nums)
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if self.no_of_subarrays(nums,mid)>k:
                low=mid+1
            else:
                high=mid-1
        return low
    def no_of_subarrays(self,nums,largestsum):
        subarrays=1
        element_sum=0
        for i in nums:
            if element_sum+i>largestsum:
                subarrays+=1
                element_sum=i
            else:
                element_sum+=i
        return subarrays



        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        