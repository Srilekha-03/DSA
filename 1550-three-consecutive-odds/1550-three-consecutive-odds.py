class Solution:
    def threeConsecutiveOdds(self, arr):
        odd_count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                odd_count += 1
            else:
                odd_count = 0
            if odd_count == 3:
                return True
        return False