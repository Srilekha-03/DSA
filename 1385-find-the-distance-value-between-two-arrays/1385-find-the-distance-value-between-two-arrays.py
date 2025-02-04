from bisect import bisect_left
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        result=0
        for num in arr1:
            idx=bisect_left(arr2, num)
            if (idx>0 and abs(num-arr2[idx-1])<=d) or (idx<len(arr2) and abs(num-arr2[idx])<=d):
                continue
            result+=1
        return result


        