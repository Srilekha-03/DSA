from collections import defaultdict
class Solution:
    def findWinners(self, matches):
        lost = defaultdict(int)
        # Count losses
        for win, lose in matches:
            lost[lose] += 1

        not_lost = []
        one_los = []

        for win, lose in matches:
            if lost[lose] == 1:
                one_los.append(lose)
            if win not in lost:
                not_lost.append(win)
                lost[win] = 2  # Mark as already added

        not_lost = sorted(set(not_lost))
        one_los = sorted(set(one_los))

        return [not_lost, one_los]
