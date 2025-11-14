from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        L = len(words[0])
        K = len(words)
        total_len = L * K

        freq = Counter(words)
        ans = []

        for offset in range(L):
            left = offset
            right = offset
            count = 0
            window = Counter()

            while right + L <= len(s):
                word = s[right:right+L]
                right += L

                if word in freq:
                    window[word] += 1
                    count += 1

                    while window[word] > freq[word]:
                        left_word = s[left:left+L]
                        window[left_word] -= 1
                        left += L
                        count -= 1

                    if count == K:
                        ans.append(left)

                else:
                    window.clear()
                    count = 0
                    left = right

        return ans
        