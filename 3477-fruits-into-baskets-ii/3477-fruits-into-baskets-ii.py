class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        count=0
        vis=[0]*n
        for i in range(n):
            is_found=0
            for j in range(n):
                if baskets[j]>=fruits[i] and vis[j]==0:
                    vis[j]=1
                    is_found=1
                    break
            if is_found==0:
                count+=1
        return count
        