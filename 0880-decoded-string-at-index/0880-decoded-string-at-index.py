class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for ch in S:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        for i in range(len(S) - 1, -1, -1):
            K %= size
            if K == 0 and S[i].isalpha():
                return S[i]
            if S[i].isdigit():
                size //= int(S[i])
            else:
                size -= 1
        return ""
