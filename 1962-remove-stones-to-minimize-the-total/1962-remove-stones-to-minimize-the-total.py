import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap=[-item for item in piles]
        heapq.heapify(max_heap)
        while k:
            largest=-heapq.heappop(max_heap)
            reduced=largest-(largest//2)
            heapq.heappush(max_heap,-reduced)
            k-=1
        return -sum(max_heap)

        