class Solution:
    def isSubsetSum(self, arr, sum):
        return self.helper(0, arr, sum)
    
    def helper(self, index, arr, target):
        # Base cases
        if target == 0:
            return True  # Found a valid subset
        if index == len(arr) or target < 0:
            return False  # No more elements or impossible target
        
        # Include current element OR exclude current element
        return (self.helper(index + 1, arr, target - arr[index]) or  # Include
                self.helper(index + 1, arr, target)) 
        
        
    
        
    
        # code here 
        
        