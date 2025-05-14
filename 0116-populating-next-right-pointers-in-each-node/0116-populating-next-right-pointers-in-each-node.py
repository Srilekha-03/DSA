"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root):
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)

            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
        return root