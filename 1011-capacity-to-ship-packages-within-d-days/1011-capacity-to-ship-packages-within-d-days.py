class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            if self.no_of_days(weights,mid)<=days:
                high=mid-1
            else:
                low=mid+1
        return low
    def no_of_days(self,weights,capacity):
        day=1
        load=0
        for i in weights:
            if i+load>capacity:
                day+=1
                load=i
            else:
                load+=i
        return day




        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        