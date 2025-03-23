class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        import heapq
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        distances = [float('inf')] * n
        ways = [0] * n
        
        distances[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > distances[node]:
                continue
            
            for neighbor, time in graph[node]:
                new_dist = dist + time
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_dist, neighbor))
                elif new_dist == distances[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % (10**9 + 7)
        
        return ways[n-1]
        
        