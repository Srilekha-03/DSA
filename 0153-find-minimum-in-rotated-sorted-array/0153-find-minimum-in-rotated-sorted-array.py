class Solution(object):
    def findMin(self, arr):
        n=len(arr)
        mini=float('inf')
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)/2
            if arr[low]<arr[high]:
                mini=min(mini,arr[low])
                return mini
            if arr[low]<=arr[mid]:
                mini=min(arr[low],mini)
                low=mid+1
            else:
                mini=min(arr[mid],mini)
                high=mid-1
        return mini

                        
        """
        :type nums: List[int]
        :rtype: int
        """
        