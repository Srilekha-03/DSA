class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validSub(sr, er, sc, ec):
            st = set()
            for row in range(sr, er):
                for col in range(sc, ec):
                    ch = board[row][col]
                    if ch == '.':
                        continue
                    if ch in st:
                        return False
                    st.add(ch)
            return True

        # check rows
        for row in range(9):
            st = set()
            for col in range(9):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ch in st:
                    return False
                st.add(ch)

        # check columns
        for col in range(9):
            st = set()
            for row in range(9):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ch in st:
                    return False
                st.add(ch)

        # check 3×3 boxes
        for sr in range(0, 9, 3):
            er = sr + 3
            for sc in range(0, 9, 3):
                ec = sc + 3
                if not validSub(sr, er, sc, ec):
                    return False

        return True
        