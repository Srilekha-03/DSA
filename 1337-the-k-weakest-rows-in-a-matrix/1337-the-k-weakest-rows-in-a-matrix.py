class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = []
        for i, row in enumerate(mat):
            count = sum(row)
            strength.append((count, i))    
        strength.sort()
        return [index for count, index in strength[:k]]
        