class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            ans = float('inf')
            for c in coins:
                ans = min(ans, 1 + helper(rem - c))
            memo[rem] = ans
            return ans
        res = helper(amount)
        return res if res != float('inf') else -1