#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        zerohead=Node(-1)
        onehead=Node(-1)
        twohead=Node(-1)
        zero=zerohead
        one=onehead
        two=twohead
        temp=head
        while temp!=None:
            if temp.data==0:
                zero.next=temp
                zero=zero.next
            elif temp.data==1:
                one.next=temp
                one=one.next
            else:
                two.next=temp
                two=two.next
            temp=temp.next
        zero.next=onehead.next if onehead.next else twohead.next
        one.next=twohead.next
        two.next=None
        return zerohead.next
        #code here
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends