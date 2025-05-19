class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        currScore = 0
        maxScore = 0      
        while l <= r:
            if P >= tokens[l]:
                P -= tokens[l]
                currScore += 1
                maxScore = max(maxScore, currScore)
                l += 1
            elif currScore >= 1:
                P += tokens[r]
                currScore -= 1
                r -= 1
            else:
                break
        
        return maxScore