class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashset= set(arr)
        result=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev=arr[i]
                cur=arr[j]
                nex=prev+cur
                length=2
                while nex in hashset:
                    length+=1
                    prev,cur=cur,nex
                    nex=prev+cur
                    result=max(result,length)
        return result

                
        