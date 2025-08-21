from collections import Counter
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mini=min(nums)
        maxi=max(nums)
        mapp=Counter(nums)
        j=0
        for i in range(mini,maxi+1):
            if i in mapp:
                element=i
                count=mapp[i]
                for k in range(count):
                    nums[j]=element
                    j+=1
        return nums


        