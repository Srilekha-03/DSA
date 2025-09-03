class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda p: (p[0], -p[1]))
        result = 0
        for i in range(n):
            x1, y1 = points[i]
            bestY = float("-inf")
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if y2 > y1:
                    continue
                if y2 > bestY:
                    result += 1
                    bestY = y2
        return result