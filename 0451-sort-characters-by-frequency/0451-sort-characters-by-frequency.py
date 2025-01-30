class Solution:
    def frequencySort(self, s: str) -> str:
        if str is None:
            return ""
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=0
            d[s[i]]+=1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
        res=""
        for key,val in sorted_dict.items():
            for i in range(val):
                res+=key
        return "".join(reversed(res))
