class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        res=[]
        for i in s:
            if not stack or stack[-1][0]!=i:
                stack.append([i,1])
            elif stack[-1][0]==i:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
        for char,freq in stack:
            res.append(char*freq)
        return "".join(res)       