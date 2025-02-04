from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        sorted_dict=dict(sorted(freq.items(),key= lambda x: (x[1],-x[0])))
        res=[]
        for k,v in sorted_dict.items():
            for i in range(v):
                res.append(k)
        return res
        