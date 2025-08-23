class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.solve(expression)

    def solve(self, s):
        result = []

        for i in range(len(s)):
            if s[i] in ['+', '-', '*']:
                left_results = self.solve(s[:i])
                right_results = self.solve(s[i+1:])

                for x in left_results:
                    for y in right_results:
                        if s[i] == '+':
                            result.append(x + y)
                        elif s[i] == '-':
                            result.append(x - y)
                        else:
                            result.append(x * y)

        if not result:
            result.append(int(s))

        return result