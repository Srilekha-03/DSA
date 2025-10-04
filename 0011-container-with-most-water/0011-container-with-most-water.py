class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxi=0
        while left<right:
            area=(right-left)*min(height[right],height[left])
            maxi=max(area,maxi)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi       