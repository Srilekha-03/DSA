class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = m - 1
        top = 0
        bottom = n - 1
        ans = []

        while left <= right and top <= bottom:
            # left to right along the top row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom along the right column
            if top <= bottom:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1

            # Traverse from right to left along the bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1): 
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from bottom to top along the left column
            if left <= right:
                for i in range(bottom, top - 1, -1): 
                    ans.append(matrix[i][left])
                left += 1

        return ans

            
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        