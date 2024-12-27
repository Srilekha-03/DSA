# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                count=1
                while slow!=fast:
                    slow=slow.next
                    count+=1
                    fast=fast.next
                return slow
        return None 
        """
        :type head: ListNode
        :rtype: ListNode
        """
        