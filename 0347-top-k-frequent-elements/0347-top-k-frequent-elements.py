from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sorted_dict= dict(sorted(freq.items(),key= lambda x: x[1],reverse=True))
        res=[]
        c=0
        for key,val in sorted_dict.items():
            if c<k:
                res.append(key)
                c+=1
            else:
                break
        return res



        