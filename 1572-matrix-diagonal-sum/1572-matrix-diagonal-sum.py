class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        summ=0
        for i in range(n):
            summ+=mat[i][i]
        j=n-1
        for i in range(n):
            if i!=j:
                summ+=mat[i][j]
            j-=1
        return summ
