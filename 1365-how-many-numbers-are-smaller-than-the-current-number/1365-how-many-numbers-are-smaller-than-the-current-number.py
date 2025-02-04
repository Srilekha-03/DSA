class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        sorted_list=sorted(nums)
        for i in range(len(nums)):
            index=sorted_list.index(nums[i])
            for j in range(index,0,-1):
                if sorted_list[j]==sorted_list[j-1]:
                    index-=1
                else:
                    break
            res.append(index)
        return res


        