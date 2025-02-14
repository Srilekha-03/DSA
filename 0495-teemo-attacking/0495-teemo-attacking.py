class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total=0
        for i in range(len(timeSeries)-1):
            total+=min(timeSeries[i+1]-timeSeries[i],duration) #either complete dur if no overlap or rest it yo
        return total+duration #as last one has no overlap so entire dur is considered