from collections import Counter
class Solution:
    def sortVowels(self, s: str) -> str:
        freq=Counter(s)
        n=len(s)
        vowel="AEIOUaeiou"
        j=0
        s_list=list(s)
        for i in range(n):
            if s_list[i] in {'A','E','I','O','U','e','a','i','o','u'}:
                while vowel[j] not in freq:
                    j+=1
                s_list[i]=vowel[j]
                freq[s_list[i]]-=1
                if freq[s_list[i]]==0:
                    del freq[s_list[i]]
        return "".join(s_list)
                
                





        