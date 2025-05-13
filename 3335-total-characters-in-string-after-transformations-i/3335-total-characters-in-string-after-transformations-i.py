class Solution:
    MOD = 10**9 + 7

    def add_mod(self, a: int, b: int) -> int:
        a += b
        if a >= self.MOD:
            a -= self.MOD
        return a

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        for _ in range(t):
            nxt = [0] * 26
            for j in range(26):
                if j < 25:
                    nxt[j+1] = freq[j]
                else:

                    nxt[0] = freq[25]
                    nxt[1] = self.add_mod(nxt[1], freq[25])
            freq = nxt

        total = 0
        for x in freq:
            total = self.add_mod(total, x)
        return total