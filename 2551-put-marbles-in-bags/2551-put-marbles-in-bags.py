class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        n = len(weights)
        cut_costs = []
        for i in range(n - 1):
            cut_costs.append(weights[i] + weights[i+1])
        
        cut_costs.sort()
        
        min_score = sum(cut_costs[:k-1])
        max_score = sum(cut_costs[-(k-1):])
        
        return max_score - min_score
        