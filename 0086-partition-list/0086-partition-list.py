# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        d1 = ListNode(-1)
        d2 = ListNode(-1)

        t = head
        t1 = d1
        t2 = d2

        while t:
            if t.val < x:
                t1.next = t
                t1 = t1.next
            else:
                t2.next = t
                t2 = t2.next
            t = t.next

        t2.next = None
        t1.next = d2.next

        return d1.next
        