class Solution:
    def findClosestPair(self,arr1, arr2, x):
        n=len(arr1)
        m=len(arr2)
        i=0
        j=m-1
        mini=float('inf')
        res=[0,0]
        while i<n and j>=0:
            summ=arr1[i]+arr2[j]
            diff=abs(summ-x)
            if diff<mini:
                mini=diff
                res=[arr1[i],arr2[j]]
            if summ>x:
                j-=1
            else:
                i+=1
        return res
        #code here