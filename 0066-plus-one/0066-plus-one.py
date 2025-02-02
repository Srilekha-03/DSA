class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry=1
        l=deque()
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==9 and carry==1:
                l.appendleft(0)
            else:
                l.appendleft(nums[i]+carry)
                carry=0
        if carry:
            l.appendleft(1)
        return list(l)
                
        
            



        