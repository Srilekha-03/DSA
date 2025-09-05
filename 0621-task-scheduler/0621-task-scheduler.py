import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        pq = [-cnt for cnt in freq.values()]
        heapq.heapify(pq)
        time = 0
        while pq:
            temp = []
            tasks_done = 0
            for _ in range(n + 1):
                if pq:
                    cnt = heapq.heappop(pq)
                    tasks_done += 1
                    if cnt + 1 < 0:
                        temp.append(cnt + 1)
            for cnt in temp:
                heapq.heappush(pq, cnt)
            time += (n + 1) if pq else tasks_done

        return time
        