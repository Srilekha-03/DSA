class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0 
        low, high = 1, max(candies)
        best = 0       
        while low <= high:
            mid = (low + high) // 2
            count = sum(c // mid for c in candies)           
            if count >= k:
                best = mid
                low = mid + 1
            else:
                high = mid - 1      
        return best
        