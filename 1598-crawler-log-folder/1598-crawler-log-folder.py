class Solution:
    def minOperations(self, logs):
        step_count = 0
        for s in logs:
            if s == "../":
                if step_count > 0:
                    step_count -= 1
            elif s == "./":
                continue
            else:
                step_count += 1
        return step_count  