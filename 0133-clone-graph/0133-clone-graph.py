"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            # Clone the current node
            clone = Node(curr.val)
            visited[curr] = clone

            # Clone all neighbors recursively
            for neigh in curr.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone

        return dfs(node)
        