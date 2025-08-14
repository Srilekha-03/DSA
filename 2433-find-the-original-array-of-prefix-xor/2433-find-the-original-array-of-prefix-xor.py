class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref) 
        for i in range(n - 1, 0, -1):
            pref[i] = pref[i] ^ pref[i - 1]
        return pref

        