class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        self.x, self.y = 0, 0

        for ch in s:
            self.addition(ch)

        st = set()
        i, j = 0, 0

        while j < k:
            self.subtraction(s[j])
            j += 1

        st.add((self.x, self.y))

        while j < n:
            self.subtraction(s[j])
            self.addition(s[i])
            st.add((self.x, self.y))
            j += 1
            i += 1

        return len(st)

    def addition(self, ch: str):
        if ch == 'U':
            self.y += 1
        elif ch == 'D':
            self.y -= 1
        elif ch == 'L':
            self.x -= 1
        else:
            self.x += 1

    def subtraction(self, ch: str):
        if ch == 'U':
            self.y -= 1
        elif ch == 'D':
            self.y += 1
        elif ch == 'L':
            self.x += 1
        else:
            self.x -= 1