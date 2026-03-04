class Solution:
    def totalElements(self, arr):
        n=len(arr)
        i=0
        j=0
        freq = {}
        ans=float('-inf')
        while j<n:
            freq[arr[j]]=freq.get(arr[j],0)+1
            if len(freq)<=2:
                ans=max(ans,j-i+1)
            else:
                freq[arr[i]]-=1
                if freq[arr[i]]==0:
                    del freq[arr[i]]
                i+=1
            j+=1
        return ans
            
        # Code here