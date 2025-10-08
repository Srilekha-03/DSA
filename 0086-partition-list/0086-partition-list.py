# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1=ListNode(-1)
        d2=ListNode(-1)
        m1=d1
        m2=d2
        curr=head
        while curr:
            if curr.val<x:
                m1.next=curr
                m1=m1.next
            else:
                m2.next=curr
                m2=m2.next
            curr=curr.next
        if not d1.next:
            return d2.next
        m1.next=d2.next
        m2.next=None
        return d1.next
        