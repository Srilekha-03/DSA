class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        return self.solve(0,low,high,zero,one)
    def solve(self,count,l,h,z,o):
        if count>h:
            return 0
        add=0
        if l<=count<=h:
            add=1
        addz=self.solve(count+z,l,h,z,o)
        addo=self.solve(count+o,l,h,z,o)
        return add+addz+addo