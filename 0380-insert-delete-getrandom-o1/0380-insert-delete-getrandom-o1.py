import random
class RandomizedSet:

    def __init__(self):
        self.arr=[]
        self.map={}
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        last_val = self.arr[-1]

        
        self.arr[index], self.arr[-1] = last_val, val
        self.map[last_val] = index

       
        self.arr.pop()
        del self.map[val]

        return True

        

    def getRandom(self) -> int:
        num=random.randint(1, 100)%len(self.arr)
        return self.arr[num] 

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()