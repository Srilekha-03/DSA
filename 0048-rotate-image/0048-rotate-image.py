class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(0,n-1):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i][0:m]=list(reversed(matrix[i][0:m]))
        return matrix

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        