
class Solution:
    def encode(self, s : str) -> str:
        if not s:
            return ""
            
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            curr = s[i]
            count = 0
            while i < n and s[i] == curr:
                i += 1
                count += 1
            result.append(curr + str(count))
                
        return "".join(result)
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.encode(s)
        
        print(res)
        

        print("~")
# } Driver Code Ends