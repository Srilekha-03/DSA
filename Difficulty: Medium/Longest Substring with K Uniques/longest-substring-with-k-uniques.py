class Solution:
    def longestKSubstr(self, s, k):
        maxi=-1
        i=0
        j=0
        n=len(s)
        d=dict()
        while j<n:
            d[s[j]]=d.get(s[j],0)+1
            if len(d)<k:
                j+=1
            elif len(d)==k:
                maxi=max(maxi,j-i+1)
                j+=1
            else:
                while len(d)>k:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1
                j+=1
            
        return maxi
        # code here
        
        