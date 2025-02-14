class ProductOfNumbers:

    def __init__(self):
        self.nums=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.nums=[1]
        else:
            self.nums.append(self.nums[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if k>=len(self.nums):
            return 0
        return self.nums[-1]//self.nums[-(k+1)]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)