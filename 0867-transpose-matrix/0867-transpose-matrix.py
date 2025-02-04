class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        transposed=[[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                transposed[j][i]=matrix[i][j]
        return transposed
        