class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        freq = {}
        max_len = -1

        for right in range(len(s)):
            # add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # shrink window if distinct > k
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # update result when exactly k distinct
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
        # code here
        
        