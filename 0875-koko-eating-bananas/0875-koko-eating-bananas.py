import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            total_hours=self.total_hours(piles,mid)
            if total_hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def total_hours(self, piles, hour):
        total = 0
        for banana in piles:
            total += (banana + hour - 1) // hour
        return total


        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        