from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.n = len(startTime)
        self.memo = [-1] * (self.n + 1)
        
        # Combine start, end, and profit into a single list of jobs
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(self.n)]
        
        # Sort jobs by start time
        jobs.sort(key=lambda x: x[0])

        # Recursive DP function
        def solve(i):
            if i >= self.n:
                return 0
            if self.memo[i] != -1:
                return self.memo[i]
            
            # Binary search: find the next job whose startTime >= current job's endTime
            l, r = i + 1, self.n - 1
            next_idx = self.n  # Default if no valid next job found
            while l <= r:
                mid = (l + r) // 2
                if jobs[mid][0] >= jobs[i][1]:
                    next_idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Option 1: Take current job
            take = jobs[i][2] + solve(next_idx)
            
            # Option 2: Skip current job
            skip = solve(i + 1)
            
            # Memoize and return
            self.memo[i] = max(take, skip)
            return self.memo[i]

        return solve(0)
