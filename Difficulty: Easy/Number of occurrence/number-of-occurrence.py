class Solution:
    def countFreq(self, nums, target):
        f=self.first( nums, target)
        if f==-1:
            return 0
        return self.last( nums, target)-f+1
            
    def first(self, nums, target):
        n=len(nums)
        first=-1
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
    def last(self, nums, target):
        n=len(nums)
        last=-1
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends