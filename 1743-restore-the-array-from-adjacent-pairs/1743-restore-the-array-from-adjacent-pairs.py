from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, node: int, prev: int, adj: dict):
        self.result.append(node)
        for neighbor in adj[node]:
            if neighbor != prev:
                self.dfs(neighbor, node, adj)

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        # Build adjacency list
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        # Find the starting point (node with only one neighbor)
        start = -1
        for node in adj:
            if len(adj[node]) == 1:
                start = node
                break

        # Do DFS starting from the start node
        self.dfs(start, float('-inf'), adj)

        return self.result
