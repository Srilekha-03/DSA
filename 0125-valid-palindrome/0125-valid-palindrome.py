class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        res=''
        for i in s:
            if i.isalnum():
                res+=i.lower()
        i=0
        j=len(res)-1
        while i<j:
            if res[i]!=res[j]:
                return False
            i+=1
            j-=1
        return True


        