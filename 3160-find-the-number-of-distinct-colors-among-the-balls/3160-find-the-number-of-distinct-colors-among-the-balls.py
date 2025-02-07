class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res=[]
        d={}
        color_count=defaultdict(int)
        unique=set()
        for key,val in queries:
            if key in d:
                oldColor=d[key]
                color_count[oldColor]-=1
                if color_count[oldColor]==0:
                    unique.discard(oldColor)
            d[key]=val
            color_count[val]+=1
            unique.add(val)
            res.append(len(unique))
        return res
            
        