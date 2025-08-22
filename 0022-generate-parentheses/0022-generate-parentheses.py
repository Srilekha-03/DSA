class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateParenthesisHelper(n, n, "", result)
        return result

    def generateParenthesisHelper(self, left, right, current, result):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            self.generateParenthesisHelper(left - 1, right, current + "(", result)
        if right > left:
            self.generateParenthesisHelper(left, right - 1, current + ")", result)

        