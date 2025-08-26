from collections import defaultdict
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        pairs=[]
        dic=defaultdict(int)
        for length,breadth in dimensions:
            area=length*breadth
            diag=(length)**2 + (breadth)**2
            pairs.append((area,diag))
        sorted_items=sorted(pairs, key=lambda x:(x[1],x[0]), reverse=True)
        return sorted_items[0][0]