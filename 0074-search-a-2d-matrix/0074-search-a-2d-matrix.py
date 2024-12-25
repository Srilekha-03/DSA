class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=m*n-1
        mid=0
        while(low<=high):
            mid=low+(high-low)//2
            row=mid/m
            col=mid%m  
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return False

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        