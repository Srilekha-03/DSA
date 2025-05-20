class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        n = len(arr)
        i = 0
        while i < n:
            j = min(i + k - 1, n - 1)
            self.reverse(arr, i, j)
            i += 2 * k
        return ''.join(arr)

    def reverse(self, arr: list, i: int, j: int) -> None:
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
