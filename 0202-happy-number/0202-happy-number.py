class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_next(n)
        return True
        