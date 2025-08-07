class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        max_len = 0
        for i in range(len(nums1)):
            for j in range(i, len(nums1)):
                sub = nums1[i:j+1]
                for k in range(len(nums2) - len(sub) + 1):
                    if nums2[k:k+len(sub)] == sub:
                        max_len = max(max_len, len(sub))
        return max_len