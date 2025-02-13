class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                if not (set(words[i]) & set(words[j])):
                    maxi=max(maxi,len(words[i])*len(words[j])) 
        return maxi       