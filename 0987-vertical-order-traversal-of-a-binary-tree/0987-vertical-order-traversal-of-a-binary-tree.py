# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):
        col_table = defaultdict(list)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            if node:
                col_table[col].append((row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        result = []
        for col in sorted(col_table.keys()):
            col_nodes = sorted(col_table[col], key=lambda x: (x[0], x[1]))
            result.append([val for row, val in col_nodes])
        
        return result

        