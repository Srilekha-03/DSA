from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        stack = sandwiches[::-1]
        queue = deque(students)
        ans = 0
        n1 = len(students)
        while stack and queue:
            dead = 0
            while queue[0] != stack[-1]:
                dead += 1
                queue.append(queue.popleft())
                if dead == len(queue):
                    return n1 - ans
            queue.popleft()
            stack.pop()
            ans += 1
        return n1 - ans