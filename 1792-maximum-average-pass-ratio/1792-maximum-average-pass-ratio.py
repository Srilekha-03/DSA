import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def delta(passed, total):
            return (passed + 1) / (total + 1) - (passed / total)
        
        pq = []
        for i, (passed, total) in enumerate(classes):
            heapq.heappush(pq, (-delta(passed, total), i))
        

        while extraStudents > 0:
            d, idx = heapq.heappop(pq)
            passed, total = classes[idx]
                      
            classes[idx][0] += 1
            classes[idx][1] += 1
            
            heapq.heappush(pq, (-delta(classes[idx][0], classes[idx][1]), idx))
            extraStudents -= 1

        result = sum(passed / total for passed, total in classes) / len(classes)
        return result
