# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
    
class MyQueue:
    def __init__(self):
        self.start = None  # Front of the queue
        self.end = None    # Rear of the queue
    
    # Function to push an element into the queue.
    def push(self, item): 
        new = Node(item)  # Create a new node with the given item
        if self.start is None:  # If the queue is empty
            self.start = new  # Both start and end point to the new node
            self.end = new
        else:  # Otherwise, add the new node at the end of the queue
            self.end.next = new
            self.end = new  # Update the end pointer
    
    # Function to pop the front element from the queue.
    def pop(self):
        if self.start is None:  # If the queue is empty
            return -1  # Return -1 as an indicator of an empty queue
        popped = self.start.data  # Get the data of the front node
        self.start = self.start.next  # Move the front pointer to the next node
        if self.start is None:  # If the queue becomes empty after popping
            self.end = None  # Reset the end pointer to None
        return popped
            
         
         #add code here


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
        print("~")
# } Driver Code Ends