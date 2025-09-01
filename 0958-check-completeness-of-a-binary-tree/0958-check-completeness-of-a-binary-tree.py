# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q=deque()
        q.append(root)
        isFound=False
        while q:
            node=q.popleft()
            if node:
                if isFound:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                isFound=True
        return True

        