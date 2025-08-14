from itertools import accumulate
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        diff=list(accumulate(shifts[::-1]))
        diff[:]=diff[::-1]
        res=""
        for i in range(len(s)):
            shift=diff[i]%26
            res+=chr((ord(s[i])-ord('a')+shift)%26+ord('a'))
        return res
