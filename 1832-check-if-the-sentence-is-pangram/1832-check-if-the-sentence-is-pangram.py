class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = [0] * 26
        for ch in sentence:
            index = ord(ch) - ord('a')
            arr[index] += 1       
        for count in arr:
            if count == 0:
                return False       
        return True
        