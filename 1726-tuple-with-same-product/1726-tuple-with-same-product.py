from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res=[]
        products=defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                if product in products:
                    for pair in products[product]:
                        res.append([pair[0],pair[1],nums[i],nums[j]])
                products[product].append([nums[i],nums[j]])
        return len(res)*8