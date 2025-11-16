class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for i in range(n)]for i in range(n)]
        res=[]

        def isSafe(row,col):
            r=row
            c=col
            for colo in range(n):
                if board[r][colo]=='Q':
                    return False
            for rowo in range(n):
                if board[rowo][c]=='Q':
                    return False
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r=row
            c=col
            while r>=0 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            r=row
            c=col
            while r<n and c>=0:
                if board[r][c]=='Q':
                    return False
                r+=1
                c-=1
            r=row
            c=col
            while r<n and c<n:
                if board[r][c]=='Q':
                    return False
                r+=1
                c+=1
            return True


        def solve(col):
            if col>=n:
                res.append(["".join(row) for row in board])
                return
            for row in range(n):
                if isSafe(row,col):
                    board[row][col]='Q'
                    solve(col+1)
                    board[row][col]='.'

        solve(0)
        return res
        