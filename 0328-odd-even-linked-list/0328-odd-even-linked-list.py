# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head 
        odd=head
        even=head.next
        evenNode=head.next
        while even==None and even.next==None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next=evenNode
        return head


        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        