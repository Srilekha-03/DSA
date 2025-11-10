class Solution:
    def jump(self, nums: List[int]) -> int:
        self.mini=float('inf')
        self.set={}
        def solve(i):
            if i>=len(nums)-1:
                return 0
            if i in self.set:
                return self.set[i]
            for j in range(1,nums[i]+1):
                self.mini=min(self.mini,1+solve(i+j))
            self.set[i]=self.mini
            return self.set[i]
        return solve(0)