class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat)
        m = len(mat[0])

        for startRow in range(n):
            arr = [1] * m
            for endRow in range(startRow, n):
                for col in range(m):
                    arr[col] &= mat[endRow][col]
                result += self.countSubarray(arr)

        return result

    def countSubarray(self, arr: List[int]) -> int:
        consecutiveOnes = 0
        subarrays = 0
        for val in arr:
            if val == 1:
                consecutiveOnes += 1
            else:
                consecutiveOnes = 0
            subarrays += consecutiveOnes
        return subarrays
        