class Solution:
    def maximum69Number (self, num: int) -> int:
        number=list(str(num))
        for i in range(len(number)):
            if number[i] == '6':
                number[i] = '9'
                break
        return int("".join(number))
        