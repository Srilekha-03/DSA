class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        stack = []
        ple = [-1] * n
        nle = [n] * n

        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Less Element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            ans += arr[i] * left * right

        return ans
        # code here
        
        