# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        prev=None
        slow=head
        fast=head
        while n>0:
            fast=fast.next
            n-=1
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        if prev==None:
            return head.next
        prev.next=prev.next.next
        return head
        

        