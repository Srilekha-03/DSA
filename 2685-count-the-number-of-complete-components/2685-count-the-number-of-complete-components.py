class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, component, visited):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component, visited)
        
        visited = [False] * n
        components = []
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component, visited)
                components.append(component)
        
        complete_count = 0
        
        for component in components:
            is_complete = True
            size = len(component)
            
            for vertex in component:
                if len(graph[vertex]) != size - 1:
                    is_complete = False
                    break
                
                for neighbor in graph[vertex]:
                    if neighbor not in component:
                        is_complete = False
                        break
                
                if not is_complete:
                    break
            
            if is_complete:
                complete_count += 1
        
        return complete_count
        