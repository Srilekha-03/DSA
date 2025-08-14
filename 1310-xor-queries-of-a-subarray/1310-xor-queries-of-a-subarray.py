class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        cumXor=[0]*n
        cumXor[0]=arr[0]
        for i in range(1,n):
            cumXor[i]=cumXor[i-1]^arr[i]
        result=[]
        for L,R in queries:
            xor_val=cumXor[R]^(0 if L==0 else cumXor[L-1])
            result.append(xor_val)
        return result