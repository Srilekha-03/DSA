from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_keys = sorted(count)
        
        for key in sorted_keys:
            if count[key] == 0:
                continue

            freq = count[key]
            for i in range(groupSize):
                if count[key + i] < freq:
                    return False
                count[key + i] -= freq

        return True
        