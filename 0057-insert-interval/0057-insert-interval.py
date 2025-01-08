class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        res=[]
        i=0
        if not intervals:
            return res.append(newInterval)
        while i<n:
            while i<n and intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
                i+=1
            while i<n and intervals[i][0]<=newInterval[1]:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                newInterval[1]=max(intervals[i][1],newInterval[1])
                i+=1
            res.append(newInterval)
            while i<n:
                res.append(intervals[i])
                i+=1
        return res


        