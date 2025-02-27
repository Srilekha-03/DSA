class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashset= {n:i for i,n in enumerate(arr)}
        result=0
        dp={} #storing (i,j) as key an len of fib as value
        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1,len(arr))):
                prev=arr[i]
                cur=arr[j]
                nex=prev+cur
                length=2
                if nex in hashset:
                    length=1+dp[(j,hashset[nex])]
                    prev,cur=cur,nex
                    nex=prev+cur
                    result=max(result,length)
                dp[(i,j)]=length
        return result

                
        