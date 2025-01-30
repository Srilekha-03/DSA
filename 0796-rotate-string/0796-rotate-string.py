class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        concatString=s+s
        if goal in concatString:
            return True
        return False
        