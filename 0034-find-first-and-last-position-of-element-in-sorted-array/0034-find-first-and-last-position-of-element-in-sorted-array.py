class Solution(object):
    def searchRange(self, arr, x):
        res=[]
        res.append(self.lb(arr,x))
        if res[0]==-1:
            return [-1,-1]
        res.append(self.ub(arr,x))
        return res
    def lb(self, arr, x):
        n=len(arr)
        ans=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                if arr[mid]==x:
                    ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def ub(self, arr, x):
        n=len(arr)
        ans=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
                
        return ans-1
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        