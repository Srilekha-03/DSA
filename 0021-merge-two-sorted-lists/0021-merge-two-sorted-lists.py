# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1=list1
        t2=list2
        dummy=ListNode(-1)
        mover=dummy
        while t1 and t2:
            if t1.val<=t2.val:
                mover.next=t1
                t1=t1.next
            else:
                mover.next=t2
                t2=t2.next
            mover=mover.next
        if t1:
            mover.next=t1
        if t2:
            mover.next=t2
        return dummy.next
        