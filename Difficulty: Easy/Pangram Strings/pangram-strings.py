#User function Template for python3
class Solution:
    def isPanagram(self, S):
        S = S.lower()
        letters = set()
        
        for ch in S:
            if 'a' <= ch <= 'z':
                letters.add(ch)
        
        return 1 if len(letters) == 26 else 0
        
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends