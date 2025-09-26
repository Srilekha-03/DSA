class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        ans=[]
        l1=[]
        l2=[]
        for num in n1:
            if num not in n2:
                l1.append(num)
        for num in n2:
            if num not in n1:
                l2.append(num)
        ans.append(l1)
        ans.append(l2)
        return ans

        