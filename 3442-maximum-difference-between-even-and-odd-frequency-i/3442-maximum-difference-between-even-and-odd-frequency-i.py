from collections import Counter
class Solution(object):
    def maxDifference(self, s):
        count = Counter(s)
        max_odd = float('-inf')
        min_even = float('inf')
        for ch, freq in count.items():
            if freq % 2 == 0:
                min_even = min(min_even, freq)
            else:
                max_odd = max(max_odd, freq)
        if max_odd == float('-inf') or min_even == float('inf'):
            return 0
        return max_odd - min_even

        
        

        """
        :type s: str
        :rtype: int
        """
        