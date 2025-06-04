class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        n=len(word)
        maxSize=n-numFriends+1
        res=""
        for i in range(n):
            currentWord=word[i:i+maxSize]
            res=max(res,currentWord)
        return res

        