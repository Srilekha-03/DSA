class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and k>0 and stack[-1]>int(i):
                stack.pop()
                k-=1
            stack.append(int(i))
        #if k doesnot exhaust after traversal
        while k:
            stack.pop()
            k-=1
        #if k==n
        if not stack:
            return "0"
        result=""
        while stack:
            result+=str(stack[-1])
            stack.pop()
        #if there are 0's
        while result and result[-1]=="0" and len(result)>len(num)-k:
            result=result[:-1]
        result=''.join(reversed(result))
        while result and result[0]=="0" and len(result)>1:
            result=result[1:]
        return result

        
        