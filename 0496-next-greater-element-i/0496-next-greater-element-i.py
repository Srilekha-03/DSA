class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngeans=self.nge(nums2)
        final=[0]*len(nums1)
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                index=nums1.index(nums2[i])
                final[index]=ngeans[i]
        return final

    def nge(self,arr):
        stack=[]
        n=len(arr)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and arr[i]>=stack[-1]:
                stack.pop()
            if not stack:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans



        