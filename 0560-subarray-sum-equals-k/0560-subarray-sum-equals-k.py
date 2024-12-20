class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        prefix=0
        d=dict()
        d[0]=1
        for i in nums:
            prefix+=i
            remaining=prefix-k
            if remaining in d:
                count+=d[remaining]

            if prefix not in d:
                d[prefix]=1
            else:
                d[prefix]+=1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        