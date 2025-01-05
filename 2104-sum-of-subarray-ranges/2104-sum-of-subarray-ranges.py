class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0
        mins=self.sumSubarrayMins(nums)
        maxs=self.sumSubarrayMaxs(nums)
        total=maxs-mins
        return total

    
    #finding min sum of all subarrays
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse=self.nse(arr)
        pse=self.pse(arr)
        total=0
        for i in range(len(arr)):
            left=i-pse[i]
            right=nse[i]-i
            total+=((left*right)*arr[i])
        return total
    def nse(self,arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else n
            stack.append(i)
        return ans
    def pse(self,arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else -1
            stack.append(i)
        return ans


    #finding max sum of all subarrays
    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        nge=self.nge(arr)
        pge=self.pge(arr)
        total=0
        for i in range(len(arr)):
            left=i-pge[i]
            right=nge[i]-i
            total+=((left*right)*arr[i])
        return total
    def nge(self,arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else n
            stack.append(i)
        return ans
    def pge(self,arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else -1
            stack.append(i)
        return ans
        