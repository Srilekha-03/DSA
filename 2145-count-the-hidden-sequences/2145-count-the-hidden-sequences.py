class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0  #just assuming a[0] - first element of the hidden sequence
        min_val = 0
        max_val = 0
        for d in differences:
            curr += d
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)
            if (upper - max_val) - (lower - min_val) + 1 <= 0:
                return 0
        return (upper - max_val) - (lower - min_val) + 1