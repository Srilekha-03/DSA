import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            total_hours=self.total_hours(piles,mid)
            if total_hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low

    def total_hours(self, piles, hour):
        total = 0
        for banana in piles:
            total += math.ceil(banana / hour)
        return total
