class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxfreq=0
        maxlen=0
        l=0
        r=0
        d=dict()
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=0
            d[s[r]]+=1
            maxfreq=max(maxfreq,d[s[r]])
            while (r-l+1)-maxfreq>k:
                d[s[l]]-=1
                if d[s[r]]==0:
                    del d[s[r]]
                maxlen=0
                for i,j in d.items():
                    maxlen=max(maxlen,j)

                l+=1
            if (r-l+1)-maxfreq<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen


        