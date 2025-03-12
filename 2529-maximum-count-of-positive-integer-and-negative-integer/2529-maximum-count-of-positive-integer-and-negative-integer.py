class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = self.first_occurrence_positive(nums)
        neg = self.last_occurrence_negative(nums)
        return max(pos, neg)

    def first_occurrence_positive(self, a):
        low, high = 0, len(a) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if a[mid] <= 0:
                low = mid + 1
            else:
                high = mid - 1
        return len(a) - low

    def last_occurrence_negative(self, a):
        low, high = 0, len(a) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if a[mid] >= 0:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1
        