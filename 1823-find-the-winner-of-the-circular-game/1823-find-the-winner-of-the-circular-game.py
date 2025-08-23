class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        i=0
        while len(arr)>1:
            ind=(i+k-1)%len(arr)
            arr.pop(ind)
            i=ind
        return arr[0]


        