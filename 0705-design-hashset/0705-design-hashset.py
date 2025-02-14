class MyHashSet:

    def __init__(self):
        self.hashSet=set()
        

    def add(self, key: int) -> None:
        self.hashSet.add(key)
        

    def remove(self, key: int) -> None:
        self.hashSet.remove(key)
        
        

    def contains(self, key: int) -> bool:
        return key in self.hashSet
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)