class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        diff=[0]*n
        for l,r in queries:
            diff[l]+=1
            if r+1<n:
                diff[r+1]-=1
        for i in range(1,n):
            diff[i]=diff[i]+diff[i-1]
        for i in range(n):
            if diff[i]<nums[i]:
                return False
        return True
        