from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sorted_dict= sorted(freq.items(),key= lambda x: x[1],reverse=True)
        res=[]
        i=0
        while k:
            res.append(sorted_dict[i][0])
            i+=1
            k-=1
        return res


        