class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        gasSum=0
        costSum=0
        for i in range(n):
            gasSum+=gas[i]
        for j in range(n):
            costSum+=cost[j]
        if costSum>gasSum:
            return -1
        ans=0
        t=0
        for i in range(n):
            t=t+gas[i]-cost[i]
            if t<0:
                t=0
                ans=i+1
        return ans




                



        