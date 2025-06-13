class Solution(object):
    def minimizeMax(self, nums, p):
        n=len(nums)
        nums.sort()
        right=max(nums)-min(nums)
        left=0
        ans=-1
        def isValid(mid):
            countPairs=0
            i=0
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=mid:
                    countPairs+=1
                    i+=2
                else:
                    i+=1
            if countPairs>=p:
                return True
            else:
                return False

        while left<=right:
            mid=left+(right-left)/2
            if isValid(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans


        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        