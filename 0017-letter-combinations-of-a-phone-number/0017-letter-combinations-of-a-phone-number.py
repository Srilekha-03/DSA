class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res=[]
        self.keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def solve(i,res):
            if len(res)==len(digits):
                self.res.append(res)
                return 
            for x in self.keypad[digits[i]]:
                solve(i+1,res+x)
        solve(0,"")
        return self.res
        