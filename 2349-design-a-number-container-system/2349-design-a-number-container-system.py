from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.index={}
        self.number={}
        

    def change(self, index: int, number: int) -> None:
        if index in self.index:
            prev=self.index[index]
            if prev in self.number:
                self.number[prev].discard(index)
                if not self.number[prev]:
                    del self.number[prev]
        self.index[index]=number
        if number not in self.number:
            self.number[number]=SortedSet()
        self.number[number].add(index)
        

    def find(self, number: int) -> int:
        if number in self.number:
            return self.number[number][0]
        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)