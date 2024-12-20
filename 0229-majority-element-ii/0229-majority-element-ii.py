class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        c1=0
        c2=0
        ele1=0
        ele2=0
        l=[]
        for i in nums:
            if c1==0 and i!=ele2:
                c1=1
                ele1=i
            elif c2==0 and ele1!=i:
                c2=1
                ele2=i
            elif i==ele1:
                c1+=1
            elif i==ele2:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=0 
        c2=0
        for i in nums:
            if i==ele1:
                c1+=1
            elif i==ele2:
                c2+=1
        if c1>n/3:
            l.append(ele1)
        if c2>n/3:
            l.append(ele2)
        return l
            

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        