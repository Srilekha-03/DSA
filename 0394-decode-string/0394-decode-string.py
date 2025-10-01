class Solution:
    def decodeString(self, s: str) -> str:
        s1=[]
        s2=[]
        num=0
        for i in s:
            if i=='[':
                s1.append(num)
                num=0
                s2.append(i)
            elif i.isdigit():
                num=num*10+int(i)
            elif i.isalpha():
                s2.append(i)
            else:
                if s1:
                    val=s1.pop()
                string=''
                while s2 and s2[-1]!="[":
                    string=s2.pop()+string
                if s2:
                    s2.pop()
                s2.append(int(val)*string)
        return "".join(s2)

            
        