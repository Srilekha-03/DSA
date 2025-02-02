class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        ans.append(1)
        x=1
        for i in range(0,rowIndex):
            x=x*(rowIndex-i)
            x=x/(i+1)
            ans.append(int(x))
        return ans



        