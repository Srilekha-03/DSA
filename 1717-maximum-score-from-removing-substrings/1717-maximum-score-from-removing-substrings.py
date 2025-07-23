class Solution:
    def modify(self, pattern: str, s: list, points: int) -> int:
        n = len(s)
        if n < 2:
            return 0
        new_s = []
        tot = 0
        for char in s:
            if new_s and new_s[-1] == pattern[0] and char == pattern[1]:
                new_s.pop()
                tot += points
            else:
                new_s.append(char)
        s[:] = new_s
        return tot
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        copy_s = list(s)
        points = 0
        if x > y:
            points += self.modify("ab", copy_s, x)
            points += self.modify("ba", copy_s, y)
        else:
            points += self.modify("ba", copy_s, y)
            points += self.modify("ab", copy_s, x)
        return points