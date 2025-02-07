class Solution:
    def shortestToChar(self,s:str,c:str)->list[int]:
        n=len(s)
        pos=-float('inf')
        answer=[float('inf')]*n
        #iter1k left to right
        for i in range(n):
            if s[i]==c:pos=i
            answer[i]=abs(i-pos)
        #right to left
        pos=float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:pos=i
            answer[i]=min(answer[i],abs(i-pos))
        return answer
