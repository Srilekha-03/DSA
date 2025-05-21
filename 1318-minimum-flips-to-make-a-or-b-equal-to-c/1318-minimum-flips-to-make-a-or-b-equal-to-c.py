class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0      
        while a != 0 or b != 0 or c != 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1
            if cbit == 1:
                if abit == 0 and bbit == 0:
                    result += 1
            else:
                result += abit + bbit
            a >>= 1
            b >>= 1
            c >>= 1
        return result
