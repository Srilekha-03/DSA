class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            divs = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)
            if len(divs) == 4:
                ans += sum(divs)
        return ans