class Solution(object):
    def minDays(self, bd, m, k):
        n=len(bd)
        if n<m*k:
            return -1
        low=min(bd)
        high=max(bd)
        while low<=high:
            mid=(low+high)//2
            if self.possible(bd,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low
    def possible(self,bd,day,m,k):
        count=0
        no_of_boq=0
        for i in bd:
            if i<=day:
                count+=1
            else:
                no_of_boq+=(count/k)
                count=0
        no_of_boq+=(count/k)
        if no_of_boq>=m:
            return True
        return False
    
        
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        