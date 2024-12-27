# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        fast=head
        slow=head
        while  fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        