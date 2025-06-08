class Solution(object):
    def partition(self, s):
        res=[]
        path=[]
        def isPalindrome(start,end):
            while start<end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        def solve(index,s,res,path):
            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if isPalindrome(index,i):
                    path.append(s[index:i+1])
                    solve(i+1,s,res,path)
                    path.pop()
        solve(0,s,res,path)
        return res

        """
        :type s: str
        :rtype: List[List[str]]
        """
        