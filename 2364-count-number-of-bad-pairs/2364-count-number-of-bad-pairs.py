class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        totat=int((n*(n-1))/2)
        good=0
        d=defaultdict(int)
        for index,val in enumerate(nums):
            diff=val-index
            good+=d[diff]
            d[diff]+=1
        return totat-good
        