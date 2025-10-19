class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.res=[]
        

    def get(self, key: int) -> int:
        for i in range(len(self.res)-1,-1,-1):
            if self.res[i][0]==key:
                temp=self.res[i]
                self.res.pop(i)
                self.res.append(temp)
                return self.res[-1][1]
        return -1
        

        
    def put(self, key: int, value: int) -> None:
        for i in range(len(self.res)):
            if self.res[i][0]==key:
                self.res.pop(i)
                self.res.append([key, value])
                return 
        if len(self.res)==self.capacity:
            self.res.pop(0)
            self.res.append([key,value])
        else:
            self.res.append([key,value])
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)