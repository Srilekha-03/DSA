class Solution(object):
    def maxele(self, mat, n, mid):
        max_val = -1
        max_index = -1
        for i in range(n):
            if mat[i][mid] > max_val:
                max_val = mat[i][mid]
                max_index = i
        return max_index

    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = low + (high - low) // 2
            row = self.maxele(mat, n, mid)
            left = -1 if mid - 1 < 0 else mat[row][mid - 1]
            right = -1 if mid + 1 >= m else mat[row][mid + 1]

            
            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1] 