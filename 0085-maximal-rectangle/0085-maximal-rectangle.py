class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        preSum=[[0]*m for i in range(n)]
        for j in range(m):
            summ=0
            for i in range(n):
                summ += int(matrix[i][j])
                if matrix[i][j]=="0":
                    preSum[i][j]=0
                else:
                    preSum[i][j]=summ
        area=0
        for i in range(n):
            area=max(area,self.largestRectangleArea(preSum[i]))
        return area

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
    

        