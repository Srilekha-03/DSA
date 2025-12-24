class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot=sum(apple)
        capacity.sort(reverse=True)
        c=0
        running=0
        for i in capacity:
            if running>=tot:
                return c
            running+=i
            c+=1
        if running>=tot:
                return c
        