class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        string=""
        openn=0
        close=0

        def solve(string,res,openn,close):
            if len(string)==2*n:               
                res.append(string)
                return 
            if openn<n:
                solve(string+"(",res,openn+1,close)
            if close<openn:
                solve(string+')',res,openn,close+1)

        solve(string,res,openn,close)
        return res
        