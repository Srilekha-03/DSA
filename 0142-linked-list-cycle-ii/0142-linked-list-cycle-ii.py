# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find(head,slow):
            pointer=head
            while pointer!=slow:
                pointer=pointer.next
                slow=slow.next
            return slow
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return find(head,slow)
        return None
            

        