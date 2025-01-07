#User function Template for python3

class Solution:
    def JobSequencing(self, ids, deadline, profit):
        jobs = [(ids[i], deadline[i], profit[i]) for i in range(len(ids))]
        jobs.sort(key=lambda x: x[2], reverse=True)
        maxDeadline = max(deadline)
        
        #parent array for DSU, initialized to its own index
        parent = list(range(maxDeadline + 1))
        
        #to find the next available slot using DSU
        def find(slot):
            if parent[slot] == slot:
                return slot
            parent[slot] = find(parent[slot])  #Path compression
            return parent[slot]
        
        total_profit = 0
        count = 0
        
        for idss, deadlines, profits in jobs:
            available_slot = find(min(deadlines, maxDeadline))
            if available_slot > 0:  # If a valid slot is available
                parent[available_slot] = find(available_slot - 1)  # Update the DSU
                count += 1
                total_profit += profits
        
        return [count, total_profit]

            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        job_ids = list(map(int, input().split()))
        deadlines = list(map(int, input().split()))
        profits = list(map(int, input().split()))
        obj = Solution()
        ans = obj.JobSequencing(job_ids, deadlines, profits)
        print(ans[0], ans[1])
        print("~")

# } Driver Code Ends