class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        arr=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j] and nums1[i] not in arr:
                arr.append(nums1[i])
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return arr
            
        