class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mini=val
        else:
            if self.mini<val:
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.mini)
                self.mini=val
                
        

    def pop(self) -> None:
        if not self.stack:
            return 
        else:
            x=self.stack.pop()
            if x<self.mini:
                self.mini=2*self.mini-x
        

    def top(self) -> int:
        if not self.stack:
            return -1
        
        x=self.stack[-1]
        if x>self.mini:
            return x
        else:
            return self.mini
        

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()