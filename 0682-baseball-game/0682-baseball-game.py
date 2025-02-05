class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in range(len(operations)):
            if operations[i]=='+':
                res.append(res[-1]+res[-2])
            elif operations[i]=='D':
                res.append(res[-1]*2)
            elif operations[i]=='C':
                res.pop()
            else:
                res.append(int(operations[i]))
        return sum(res)
        