from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=Counter(arr)
        return len(set(d.values()))==len(d.values())

        