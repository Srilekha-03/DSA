class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        suf=[0]*(n+1)
        for i in range(1,n+1):
            suf[i]=gain[i-1]+suf[i-1]
        return max(suf)
        