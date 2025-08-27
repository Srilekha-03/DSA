from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        freq=Counter(nums)
        for i in range(1,n+1):
            if freq[i]==0:
                sec=i
            elif freq[i]==2:
                fir=i
        res.append(fir)
        res.append(sec)
        return res
        