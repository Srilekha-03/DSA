class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def conversion_to_minutes(time:str)->int:
            h,m=map(int,time.split(":"))
            return h*60+m
        minutes_sorted=sorted(conversion_to_minutes(t) for t in timePoints)
        mini=float("inf")
        for i in range(1,len(minutes_sorted)):
            mini=min(mini,minutes_sorted[i]-minutes_sorted[i-1])
        circular_diff=1440-(minutes_sorted[-1]-minutes_sorted[0])
        return min(mini,circular_diff)
        