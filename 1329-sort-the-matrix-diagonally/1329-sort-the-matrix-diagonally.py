from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        dic=defaultdict(list)
        for i in range(n):
            for j in range(m):
                dic[i-j].append(mat[i][j])
        for val in dic.values():
            val.sort()
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                mat[i][j]=dic[i-j].pop()
        return mat


        