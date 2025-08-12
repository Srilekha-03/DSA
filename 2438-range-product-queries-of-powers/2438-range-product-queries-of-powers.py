class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers=[]
        for i in range(32):
            if n&(1<<i)!=0:
                powers.append(2**i)
        res=[]
        for i in queries:
            start=i[0]
            end=i[1]
            product=1
            for i in range(start,end+1):
                product*=powers[i]
            res.append(product)
        return res

        