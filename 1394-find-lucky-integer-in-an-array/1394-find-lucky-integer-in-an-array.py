class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        maxi=-1
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=0
            d[arr[i]]+=1
        for key,value in d.items():
            if key==value:
                maxi=max(key,maxi)
        return maxi

        