class Solution:
    def __init__(self):
        self.mp = {}

    def solve(self, s1: str, s2: str) -> bool:
        if s1 == s2:  # both empty or identical
            return True
        if len(s1) != len(s2):
            return False

        key = s1 + "_" + s2
        if key in self.mp:
            return self.mp[key]

        n = len(s1)
        result = False

        for i in range(1, n):
            # Case 1: Swapped
            swapped = (self.solve(s1[:i], s2[n-i:]) and
                       self.solve(s1[i:], s2[:n-i]))
            if swapped:
                result = True
                break

            # Case 2: Not swapped
            not_swapped = (self.solve(s1[:i], s2[:i]) and
                           self.solve(s1[i:], s2[i:]))
            if not_swapped:
                result = True
                break

        self.mp[key] = result
        return result

    def isScramble(self, s1: str, s2: str) -> bool:
        self.mp.clear()
        return self.solve(s1, s2)

        