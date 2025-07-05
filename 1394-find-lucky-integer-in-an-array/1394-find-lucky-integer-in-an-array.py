from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxi=-1
        d=Counter(arr)
        for key,value in d.items():
            if key==value:
                maxi=max(key,maxi)
        return maxi

        