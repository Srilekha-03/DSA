import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        indexed_tasks.sort()  #sort by enqueueTime

        res = []
        time = 0
        i = 0
        min_heap = []

        while i < n or min_heap:
            if not min_heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(min_heap, (process, idx)) 
                i += 1

            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            res.append(idx)

        return res
        