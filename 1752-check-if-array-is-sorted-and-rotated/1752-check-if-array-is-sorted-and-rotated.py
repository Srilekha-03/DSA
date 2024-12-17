class Solution(object):
    def check(self, arr):
        s=arr[0]
        d=0
        for i in range(len(arr)):
            if arr[i]<s:
                s=arr[i]
                d=i
        for i in range(1,d):
            if arr[i]<arr[i-1]:
                return False
        for i in range(d+1,len(arr)):
            if arr[i]<arr[i-1]:
                return False
        return True  
        
                
        """
        :type nums: List[int]
        :rtype: bool
        """
        