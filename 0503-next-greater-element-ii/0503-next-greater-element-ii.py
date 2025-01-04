class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        stack=[]
        n=len(arr)
        ans=[0]*n
        for i in range(2*n-1,-1,-1):
            while stack and arr[i%n]>=stack[-1]:
                stack.pop()
            if i<n:
                if not stack:
                    ans[i]=-1
                else:
                    ans[i]=stack[-1]
            stack.append(arr[i%n])
        return ans
        