from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for i in range(1,n+1):
            q.append(i)
        while len(q)>1:
            for i in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q.popleft()




        