class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        
        change = [[0] * m for _ in range(n)]
        
        diri = [-1, -1, -1, 0, 1, 1, 1, 0]
        dirj = [-1, 0, 1, 1, 1, 0, -1, -1]
        
        for i in range(n):
            for j in range(m):
                count = 0
                
                for k in range(8):
                    ni = i + diri[k]
                    nj = j + dirj[k]
                    
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 1:
                        count += 1
                
                # live cell dies if not 2 or 3 neighbors
                if board[i][j] == 1 and count not in (2, 3):
                    change[i][j] = 1
                
                # dead cell becomes alive if count == 3
                elif board[i][j] == 0 and count == 3:
                    change[i][j] = 1
        
        # apply changes
        for i in range(n):
            for j in range(m):
                if change[i][j] == 1:
                    board[i][j] = 0 if board[i][j] == 1 else 1

        """
        Do not return anything, modify board in-place instead.
        """
        