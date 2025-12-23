import bisect
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n=len(events)
        starts=[e[0] for e in events]
        suffix=[0]*n
        suffix[-1]=events[-1][2]
        for i in range(n-2,-1,-1):
            suffix[i]=max(suffix[i+1],events[i][2])
        ans=0
        for i in range(n):
            ans=max(ans,events[i][2])
            j=bisect.bisect_left(starts,events[i][1]+1)
            if j<n:
                ans=max(ans,events[i][2]+suffix[j])
        return ans