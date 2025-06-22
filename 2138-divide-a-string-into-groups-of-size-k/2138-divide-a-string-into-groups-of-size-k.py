class Solution(object):
    def divideString(self, s, k, fill):
        ans=[]
        n=len(s)
        remainder=n%k
        if remainder!=0:
            s+=fill*(k-remainder)

        m=len(s)
        for i in range(0,m,k):
            group=s[i:i+k]
            ans.append(group)
        return ans

        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        