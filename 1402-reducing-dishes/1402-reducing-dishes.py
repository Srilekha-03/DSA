class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        memo = {}

        def solve(i: int, time: int) -> int:
            if i == n:
                return 0
            if (i, time) in memo:
                return memo[(i, time)]

            include = satisfaction[i] * time + solve(i + 1, time + 1)
            exclude = solve(i + 1, time)
            memo[(i, time)] = max(include, exclude)
            return memo[(i, time)]

        return solve(0, 1)