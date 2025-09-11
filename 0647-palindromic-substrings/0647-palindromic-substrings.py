class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]

        for i in range(n):
            for j in range(i, n):
                if isPalindrome(s[i:j+1]):
                    count += 1

        return count
        