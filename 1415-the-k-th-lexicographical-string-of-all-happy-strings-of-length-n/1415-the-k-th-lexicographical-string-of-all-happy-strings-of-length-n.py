class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        chars = ['a', 'b', 'c']       
        def backtrack(curr_string):
            if len(curr_string) == n:
                happy_strings.append(curr_string)
                return
            for ch in chars:
                if not curr_string or curr_string[-1] != ch: 
                    backtrack(curr_string + ch)       
        backtrack("")       
        return happy_strings[k - 1] if k <= len(happy_strings) else ""
        