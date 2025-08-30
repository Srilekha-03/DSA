class Solution:
    def validSub(self, board: List[List[str]], sr: int, er: int, sc: int, ec: int) -> bool:
        st = set()
        for row in range(sr, er + 1):
            for col in range(sc, ec + 1):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ch in st:
                    return False
                st.add(ch)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            st = set()
            for col in range(9):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ch in st:
                    return False
                st.add(ch)

        for col in range(9):
            st = set()
            for row in range(9):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ch in st:
                    return False
                st.add(ch)

        for sr in range(0, 9, 3):
            er = sr + 2
            for sc in range(0, 9, 3):
                ec = sc + 2
                if not self.validSub(board, sr, er, sc, ec):
                    return False

        return True

        