from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        n=len(s)
        vowels=['a','e','i','o','u']
        freq=Counter(s)
        vowelFreq=0
        consfreq=0
        for char,count in freq.items():
            if char in vowels:
                vowelFreq=max(vowelFreq,count)
                
        for char,count in freq.items():
            if char not in vowels:
                consfreq=max(consfreq,count)
        return vowelFreq+consfreq

        