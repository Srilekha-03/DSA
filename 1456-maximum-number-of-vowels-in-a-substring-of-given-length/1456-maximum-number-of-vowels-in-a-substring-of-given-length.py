class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        vow=['a','i','e','o','u']
        i=0
        j=0
        count=0
        maxi=0
        while j<n:
            if s[j] in vow:
                count+=1
            if j-i+1==k:
                maxi=max(maxi,count)
                if s[i] in vow:
                    count-=1
                i+=1
            j+=1
        return maxi

        