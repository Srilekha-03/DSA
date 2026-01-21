class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        i=0
        j=0
        mem=dict()
        def solve(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j) in mem:
                return mem[(i,j)]
            if nums1[i]==nums2[j]:
                mem[(i,j)]=1+solve(i+1,j+1)
                return mem[(i,j)]
            else:
                mem[(i,j)]=max(solve(i+1,j),solve(i,j+1))
                return mem[(i,j)]
        return solve(0,0)

        