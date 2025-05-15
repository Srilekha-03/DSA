class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        i = 0
        index = 0
        while i < n:
            curr = chars[i]
            count = 0
            while i < n and chars[i] == curr:
                i += 1
                count += 1
            #assigning here
            chars[index] = curr
            index += 1
            if count > 1:
                for ch in str(count):
                    chars[index] = ch
                    index += 1
        return index