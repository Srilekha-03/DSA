class Solution(object):
    def maxDistance(self, s, k):
        max_md = 0
        east = west = north = south = 0
        for i in range(len(s)):
            if s[i] == 'E':
                east += 1
            elif s[i] == 'W':
                west += 1
            elif s[i] == 'N':
                north += 1
            elif s[i] == 'S':
                south += 1
            curr_md = abs(east - west) + abs(north - south)
            steps = i + 1
            wasted = steps - curr_md
            extra = min(2 * k, wasted)
            final_current_md = curr_md + extra
            max_md = max(max_md, final_current_md)

        return max_md
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        