class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        maxi=float('-inf')
        for i in st:
            if i-1 not in st:
                count=0
                x=i
                while x+1 in st:
                    count+=1
                    x+=1
                maxi=max(maxi,count+1)
        return maxi

        