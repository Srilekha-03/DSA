class Solution:
    def minTimeToReach(self, moveTime):
        r, c = len(moveTime), len(moveTime[0])
        minimumTime = [[float('inf')] * c for _ in range(r)]
        pq = []
        # (steps, i, j, move)
        heapq.heappush(pq, (-1, 0, 0, 1))
        minimumTime[0][0] = 0

        def update(i, j, steps, move):
            nextStep = move + max(steps, moveTime[i][j])
            if minimumTime[i][j] > nextStep:
                heapq.heappush(pq, (nextStep, i, j, 2 if move == 1 else 1))
                minimumTime[i][j] = nextStep

        while pq:
            steps, i, j, move = heapq.heappop(pq)

            if i + 1 < r: update(i + 1, j, steps, move)
            if i - 1 >= 0: update(i - 1, j, steps, move)
            if j + 1 < c: update(i, j + 1, steps, move)
            if j - 1 >= 0: update(i, j - 1, steps, move)

            if minimumTime[r - 1][c - 1] != float('inf'):
                return minimumTime[r - 1][c - 1]

        return -1