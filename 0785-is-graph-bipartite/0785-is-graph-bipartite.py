class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0 
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = int(not color[node])
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False 
        return True
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        