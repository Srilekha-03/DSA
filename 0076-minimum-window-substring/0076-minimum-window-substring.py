from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        if m>n:
            return ""
        dic=defaultdict(int)
        for i in t:
            dic[i]+=1
        i=0
        j=0
        count=m
        min_window=float('inf')
        start_index=0
        while j<n:
            if dic[s[j]]>0:
                count-=1
            dic[s[j]]-=1
            while count==0:
                if min_window>j-i+1:
                    min_window=j-i+1
                    start_index=i
                dic[s[i]]+=1
                if dic[s[i]]>0:
                    count+=1
                i+=1
            j+=1
        return "" if min_window==float('inf') else s[start_index:start_index+min_window]


