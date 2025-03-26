class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array=[]
        remainder=grid[0][0]%x
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]%x!=remainder:
                    return -1
                array.append(grid[i][j])
        n=len(array)
        array.sort()
        median=n//2
        for i in array:
            count+=abs(i-array[median])//x
        return count
        