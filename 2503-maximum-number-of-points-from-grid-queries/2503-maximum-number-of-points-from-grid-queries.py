import heapq

def maxPoints(grid, queries):
    m, n = len(grid), len(grid[0])
    sorted_queries = sorted(queries)
    query_result = {}
    answer = [0] * len(queries)

    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    min_heap = [(grid[0][0], 0, 0)]
    visited = set()
    visited.add((0,0))

    points = 0

    for query in sorted_queries:
        while min_heap and min_heap[0][0] < query:
            val, r, c = heapq.heappop(min_heap)
            points += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

        query_result[query] = points

    for i, q in enumerate(queries):
        answer[i] = query_result[q]

    return answer