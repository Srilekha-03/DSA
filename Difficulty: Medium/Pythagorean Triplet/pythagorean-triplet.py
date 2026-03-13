class Solution:
	def pythagoreanTriplet(self, arr):
	    n = len(arr)

        squares = [x*x for x in arr]
        s = set(squares)

        for i in range(n):
            for j in range(i+1, n):
                if squares[i] + squares[j] in s:
                    return True

        return False
    	# code here