from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n=len(changed)
        if n%2!=0:
            return []
            
        changed.sort()
        mp=Counter(changed)
        res=[]
        for num in changed:
            if mp[num]==0:
                continue
            if mp[2*num]==0:
                return []
            res.append(num)
            mp[num]-=1
            mp[2*num]-=1
        return res
