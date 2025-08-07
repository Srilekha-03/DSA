class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        # Try all possible numbers of unique characters (1 to 26 for lowercase letters)
        for target_unique in range(1, 27):
            freq = [0] * 26  # Frequency of a-z
            left = 0
            right = 0
            unique = 0  # Current number of unique characters
            count_at_least_k = 0  # Unique chars with frequency ≥ k

            while right < len(s):
                # Expand the window
                if unique <= target_unique:
                    idx = ord(s[right]) - ord('a')
                    if freq[idx] == 0:
                        unique += 1
                    freq[idx] += 1
                    if freq[idx] == k:
                        count_at_least_k += 1
                    right += 1
                else:
                    # Shrink the window
                    idx = ord(s[left]) - ord('a')
                    if freq[idx] == k:
                        count_at_least_k -= 1
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        unique -= 1
                    left += 1

                # Update result if valid
                if unique == target_unique and unique == count_at_least_k:
                    max_len = max(max_len, right - left)
        return max_len