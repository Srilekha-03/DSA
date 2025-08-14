class Solution:
    def largestGoodInteger(self, num: str) -> str:
        seq=[str(i)*3 for i in range(10)]
        for i in range(9,-1,-1):
            if seq[i] in num:
                return seq[i]
        return ""
        