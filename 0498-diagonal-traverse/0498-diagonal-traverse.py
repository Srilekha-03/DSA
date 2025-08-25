from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        ans=[]
        dic=defaultdict(list)
        for i in range(n):
            for j in range(m):
                dic[i+j].append(mat[i][j])
        for key,val in dic.items():
            if key%2==0:
                val.reverse()
            ans.extend(val)
        return ans
        
        