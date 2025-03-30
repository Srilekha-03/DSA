class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        partitions = []
        start, end = 0, 0

        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        
        return partitions
        