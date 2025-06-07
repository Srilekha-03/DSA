class Solution:
    def clearStars(self, s: str) -> str:
        import heapq

        to_be_removed = set()
        min_heap = []

        for i, ch in enumerate(s):
            if ch == '*':
                out = heapq.heappop(min_heap)
                to_be_removed.add(-out[1])  # character index
                to_be_removed.add(i)        # '*' index
            else:
                heapq.heappush(min_heap, (ch, -i))  # push char with -index

        # Build the result string excluding removed indices
        result = ''.join(s[i] for i in range(len(s)) if i not in to_be_removed)
        return result
