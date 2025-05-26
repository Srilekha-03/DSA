# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            right_node = None
            for _ in range(n):
                right_node = queue.popleft()
                if right_node.left:
                    queue.append(right_node.left)
                if right_node.right:
                    queue.append(right_node.right)
            result.append(right_node.val)
        return result