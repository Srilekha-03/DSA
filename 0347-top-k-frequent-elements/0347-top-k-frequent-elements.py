import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        max_heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(max_heap)
        result = []
        for i in range(k):
            count, num = heapq.heappop(max_heap)
            result.append(num)
        return result

        