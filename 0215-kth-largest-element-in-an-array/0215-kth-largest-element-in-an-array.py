import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap=nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            heapq.heappush(min_heap,num)
            if len(min_heap)>k:
                 heapq.heappop(min_heap)
        return min_heap[0]
        