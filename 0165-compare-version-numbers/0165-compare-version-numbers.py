class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1=version1.split(".")
        l2=version2.split(".")
        n1=len(l1)
        n2=len(l2)
        i=0
        while i<max(n1,n2):
            num1=0
            if i<n1:
                num1=l1[i]
            num2=0
            if i<n2:
                num2=l2[i]
            if int(num1)>int(num2):
                return 1
            elif int(num1)<int(num2):
                return -1
            i+=1
        return 0
