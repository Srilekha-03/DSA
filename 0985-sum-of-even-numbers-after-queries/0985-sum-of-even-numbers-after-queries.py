class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumEven=0
        for x in nums:
            if x%2==0:
                sumEven+=x
        result=[]
        for val,idx in queries:
            if nums[idx]%2==0:
                sumEven-=nums[idx]
            nums[idx]+=val
            if nums[idx]%2==0:
                sumEven+=nums[idx]
            result.append(sumEven)
        return result