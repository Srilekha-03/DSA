class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestArea=0
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                index=stack[-1]
                nse=i
                stack.pop()
                pse=stack[-1] if stack else -1
                largestArea=max(largestArea, heights[index]*(nse-pse-1))
            stack.append(i)
        while stack:
            nse=len(heights)
            index=stack[-1]
            stack.pop()
            pse=stack[-1] if stack else -1
            largestArea=max(largestArea, heights[index]*(nse-pse-1))
        return largestArea


        