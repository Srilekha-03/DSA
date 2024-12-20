class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)
        maxlen=0
        count=0
        st=set()
        for i in nums:
            st.add(i)
        for i in st:
            if i-1 not in st:
                count=1
                x=i
                while x+1 in st:
                    count+=1
                    x=x+1
            maxlen=max(maxlen,count)
        return maxlen
        """
        :type nums: List[int]
        :rtype: int
        """
        