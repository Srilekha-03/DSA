class Solution(object):
    def floodFill(self, image, sr, sc, color):
        duplicate=[row[:] for row in image]
        initial=image[sr][sc]
        n=len(image)
        m=len(image[0])
        rows=[-1,0,+1,0]
        cols=[0,+1,0,-1]
        def dfs(sr,sc):
            duplicate[sr][sc]=color
            for i in range(4):
                newrow=sr+rows[i]
                newcol=sc+cols[i]
                if newrow>=0 and newrow<n and newcol>=0 and newcol<m and duplicate[newrow][newcol]!=color and image[newrow][newcol]==initial:
                    dfs(newrow,newcol) 

        dfs(sr,sc)
        return duplicate
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        