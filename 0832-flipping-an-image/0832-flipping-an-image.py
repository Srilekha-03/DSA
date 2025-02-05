class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for j in range(len(row)):  
                row[j]^=1 
        return image
        