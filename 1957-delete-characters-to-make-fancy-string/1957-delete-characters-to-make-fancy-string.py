class Solution:
    def makeFancyString(self, s: str) -> str:
        duplicate=""
        for i in s:
            if len(duplicate)<2:
                duplicate+=i
            else :
                if i==duplicate[-1] and i==duplicate[-2]:
                    pass
                else:
                    duplicate+=i
        return duplicate
            

        