class Solution:
    def checkFreq(self, s: str) -> bool:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
            if freq[ord(ch) - ord('a')] > 1:
                return True
        return False

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return self.checkFreq(s)
        indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indices.append(i)
        if len(indices) != 2:
            return False
        i, j = indices
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        return "".join(s_list) == goal
