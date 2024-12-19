class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        n=len(nums)

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        c1=0
        for i in nums:
            if i==candidate:
                c1+=1
        if c1>n/2:
            return candidate

        return -1
