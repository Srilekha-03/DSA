import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pq = []
        for i in range(m):
            for j in range(n):
                s = nums1[i] + nums2[j]
                if len(pq) < k:
                    heapq.heappush(pq, (-s, i, j))
                elif -pq[0][0] > s:
                    heapq.heappop(pq)
                    heapq.heappush(pq, (-s, i, j))
                else:
                    break
        result = []
        while pq:
            s, i, j = heapq.heappop(pq)
            result.append([nums1[i], nums2[j]])
        return result