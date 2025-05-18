class Solution:
    def largestVariance(self, s: str) -> int:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1       
        result = 0
        for first in range(ord('a'), ord('z') + 1):
            for second in range(ord('a'), ord('z') + 1):
                first_idx = first - ord('a')
                second_idx = second - ord('a')
                
                if count[first_idx] == 0 or count[second_idx] == 0:
                    continue
                
                if first == second:
                    continue
                
                first_count = 0
                second_count = 0
                past_low_freq = False
                
                for ch in s:
                    if ord(ch) == first:
                        first_count += 1
                    if ord(ch) == second:
                        second_count += 1
                    
                    if second_count > 0:
                        result = max(result, first_count - second_count)
                    elif past_low_freq:
                        result = max(result, first_count - 1)
                    
                    if second_count > first_count:
                        second_count = 0
                        first_count = 0
                        past_low_freq = True
        
        return result