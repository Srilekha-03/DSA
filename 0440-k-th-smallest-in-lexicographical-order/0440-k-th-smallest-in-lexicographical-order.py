class Solution(object):
    def findKthNumber(self, n, k):
        self.k=k
        self.result=None
        def solve(cur,n):
            if cur>n:
                return
            self.k-=1
            if self.k==0:
                self.result=cur
            for i in range(10):
                new_num=cur*10+i
                if new_num>n:
                    break
                solve(new_num,n)
        for i in range(1, 10):
            solve(i,n)
            if self.result is not None:
                break 
        return self.result
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        