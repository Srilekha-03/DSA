class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        prefixXor=[0]*(n+1)
        for i in range(1,n+1):
            prefixXor[i]=prefixXor[i-1]^arr[i-1]
        count=0
        for i in range(n+1):
            for k in range(i+1,n+1):
                if prefixXor[k]==prefixXor[i]:
                    count+=k-i-1
        return count
        