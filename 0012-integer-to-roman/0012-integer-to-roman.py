class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]      
        result = ""
        i = 0
        while num > 0:
            while num >= val[i]:
                num -= val[i]
                result += sym[i]
            i += 1
        return result
        