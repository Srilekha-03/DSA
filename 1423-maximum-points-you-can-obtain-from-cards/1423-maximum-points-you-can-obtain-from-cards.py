class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum=0
        maxSum=0
        rightSum=0
        for i in range(k):
            leftSum+=cardPoints[i]
        maxSum=leftSum
        r=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            leftSum-=cardPoints[i]
            rightSum+=cardPoints[r]
            r-=1
            maxSum=max(maxSum,leftSum+rightSum)
        return maxSum

            
            
        