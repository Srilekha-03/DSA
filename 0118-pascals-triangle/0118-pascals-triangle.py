class Solution(object):
    def generate(self, numRows):
        n=numRows
        vector=[]
        for i in range(1,n+1):
            vector.append(self.generateRow(i))
        return vector
    def generateRow(self,n):
        rowlist=[]
        ans=1
        rowlist.append(1)
        for i in range(1,n):
            ans*=(n-i)
            ans/=i
            rowlist.append(ans)
        return rowlist
        



        
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        