class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: (x[0], x[1]))
        
        intervals = [points[0]]
        e = points[0][1]

        for i in range(1, n):
            sc, ec = points[i]
            if e >= sc:
                # Merge overlapping intervals
                intervals[-1][1] = max(intervals[-1][1], ec)
                e = min(e, ec)
            else:
                # Start a new interval
                intervals.append([sc, ec])
                e = ec
        return len(intervals)
        