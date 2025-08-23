from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_len = len(p)
        s_len = len(s)
        if p_len > s_len:
            return result

        p_counter = Counter(p)
        window_counter = Counter(s[:p_len])

        if window_counter == p_counter:
            result.append(0)

        for i in range(1, s_len - p_len + 1):
            start_char = s[i - 1]
            end_char = s[i + p_len - 1]
            window_counter[start_char] -= 1
            if window_counter[start_char] == 0:
                del window_counter[start_char]
            window_counter[end_char] += 1
            if window_counter == p_counter:
                result.append(i)
        return result