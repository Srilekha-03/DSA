class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=0
        n=len(nums)
        ele1,ele2=None,None
        for num in nums:
            if c1==0 and num!=ele2:
                ele1=num
            if c2==0 and num!=ele1:
                ele2=num
            if num==ele1:
                c1+=1
            elif num==ele2:
                c2+=1
            else:
                c1-=1
                c2-=1
        res=[]
        c1=0
        c2=0
        for num in nums:
            if num==ele1:
                c1+=1
            elif num==ele2:
                c2+=1
        if c1>n//3:
            res.append(ele1)
        if c2>n//3:
            res.append(ele2)
        return res

        

        