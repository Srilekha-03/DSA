class SmallestInfiniteSet:
    def __init__(self):
        self.nums = [True] * 1001
        self.i = 1

    def popSmallest(self) -> int:
        result = self.i
        self.nums[self.i] = False

        for j in range(self.i + 1, 1001):
            if self.nums[j]:
                self.i = j
                break

        return result

    def addBack(self, num: int) -> None:
        self.nums[num] = True
        if num < self.i:
            self.i = num

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)