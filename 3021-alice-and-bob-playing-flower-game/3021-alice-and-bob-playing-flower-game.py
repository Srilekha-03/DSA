class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if n%2:
            even=n//2
            odd=n-even
        else:
            even=n//2
            odd=even
        ans=0
        for i in range(1,m+1):
            if i%2:
                ans+=even
            else:
                ans+=odd
        return ans

        