class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=1
        n=len(intervals)
        end=intervals[0]
        for i in range(1,n):
            if intervals[i][0]>=end[1]:
                count+=1
                end=intervals[i]
        return n-count

        