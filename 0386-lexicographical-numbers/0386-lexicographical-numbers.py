class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        def solve(cur,n,res):
            if cur>n:
                return
            res.append(cur)
            for i in range(10):
                new_num=cur*10+i
                if new_num>n:
                    return
                solve(new_num,n,res)
       
        for start in range(1,10):
            solve(start,n,res)
        return res

        