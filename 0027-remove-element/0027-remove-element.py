class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dup=[]
        for i in nums:
            if i!=val:
                dup.append(i)
        n=len(dup)
        nums[:n]=dup[:]
        return n
        