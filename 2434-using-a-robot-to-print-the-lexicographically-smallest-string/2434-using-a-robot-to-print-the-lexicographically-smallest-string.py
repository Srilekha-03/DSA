class Solution:
    def robotWithString(self, s: str) -> str:
        t = []  #acts as Stack
        paper = []
        n = len(s)  
        #Precomputing minSuffix
        minSuffix = ['z'] * (n + 1)
        for i in range(n - 1, -1, -1):
            minSuffix[i] = min(minSuffix[i + 1], s[i])
        
        for i in range(n):
            t.append(s[i])  #push onto stack
            while t and t[-1] <= minSuffix[i + 1]:
                paper.append(t.pop())

        return ''.join(paper)
