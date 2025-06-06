from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def next_permutation(arr):
            i=len(arr)-2
            while i>=0 and arr[i]>=arr[i+1]: i-=1
            if i==-1: return False
            j=len(arr)-1
            while arr[j]<=arr[i]: j-=1
            arr[i],arr[j]=arr[j],arr[i]
            arr[i+1:]=reversed(arr[i+1:])
            return True

        nums.sort()
        res=[nums[:]]
        while next_permutation(nums): res.append(nums[:])
        return res
        