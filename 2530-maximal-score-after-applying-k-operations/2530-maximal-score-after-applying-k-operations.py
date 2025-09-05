import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[-i for i in nums]
        heapq.heapify(heap)
        res=0
        while k:
            maxi=-heapq.heappop(heap)
            res+=maxi
            heapq.heappush(heap,-math.ceil(maxi/3))
            k-=1
        return res


        

        