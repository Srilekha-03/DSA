class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Step 1: Find all mismatching bit positions
        result = (a | b) ^ c

        # Step 2: Bits where both a and b are 1
        result1 = a & b

        # Step 3: Positions needing 2 flips (both are 1 but c=0)
        result2 = result1 & result

        # Step 4: Count bits (Python 3.10+ has int.bit_count())
        return result.bit_count() + result2.bit_count()