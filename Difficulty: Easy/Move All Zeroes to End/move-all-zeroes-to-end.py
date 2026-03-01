class Solution:
	def pushZerosToEnd(self, arr):
	    n=len(arr)
	    i=0
	    for x in range(n):
	        if arr[x]==0:
	            i=x
	            break
	    j=x+1
	    while i<n and j<n:
	        if arr[j]!=0:
	            arr[i],arr[j]=arr[j],arr[i]
	            i+=1
	            j+=1
	        else:
	            j+=1
	    
	            
	            
    	# code here