class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        count=0
        for i in range(31):
            if ans & 1<<i:
                count+=1
        return count
        