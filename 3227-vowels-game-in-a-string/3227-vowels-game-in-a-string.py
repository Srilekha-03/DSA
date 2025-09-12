class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in s:
            if i in ['a','e','i','o','u']:
                return True
        return False

        