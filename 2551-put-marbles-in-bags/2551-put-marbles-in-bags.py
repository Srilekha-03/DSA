class Solution:
   def putMarbles(self, weights: List[int], k: int) -> int:
       if k == 1:
           return 0
       
       n = len(weights)
       cut_costs = [weights[i] + weights[i+1] for i in range(n-1)]
       
       import heapq
       
       min_heap = cut_costs.copy()
       heapq.heapify(min_heap)
       min_score = sum(heapq.heappop(min_heap) for _ in range(k-1))
       
       max_heap = [-cost for cost in cut_costs]
       heapq.heapify(max_heap)
       max_score = sum(-heapq.heappop(max_heap) for _ in range(k-1))
       
       return max_score - min_score