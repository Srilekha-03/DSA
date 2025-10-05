class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=[1]*(n+1)
        i2=i3=i4=1
        for i in range(2,n+1):
            i2v=arr[i2]*2
            i3v=arr[i3]*3
            i4v=arr[i4]*5
            mini=min(i2v,i3v,i4v)
            arr[i]=mini
            if mini==i2v:
                i2+=1
            if mini==i3v:
                i3+=1
            if mini==i4v:
                i4+=1
        return arr[n]

        