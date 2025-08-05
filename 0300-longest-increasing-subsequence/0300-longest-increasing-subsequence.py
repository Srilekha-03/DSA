class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        temp=[]
        temp.append(nums[0])
        def lower_bound(temp,ele):
            l=0
            h=len(temp)-1
            while l<=h:
                m=l+(h-l)//2
                if temp[m]>=ele:
                    h=m-1
                else:
                    l=m+1
            return l
        for i in range(1,n):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                index=lower_bound(temp,nums[i])
                temp[index]=nums[i]
        return len(temp)

        