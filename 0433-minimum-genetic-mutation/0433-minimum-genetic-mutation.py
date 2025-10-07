from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankset = set(bank)
        visited = set([start])
        q = deque([start])
        level = 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == end:
                    return level
                for ch in "ACGT":
                    for i in range(len(curr)):
                        neighbour = curr[:i] + ch + curr[i+1:]
                        if neighbour not in visited and neighbour in bankset:
                            visited.add(neighbour)
                            q.append(neighbour)
            level += 1
        return -1
