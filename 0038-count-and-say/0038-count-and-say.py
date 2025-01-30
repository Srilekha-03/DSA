class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            new_result = ""
            count = 1
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    new_result += str(count) + result[i - 1]
                    count = 1
            new_result += str(count) + result[-1]
            result = new_result
        return result
