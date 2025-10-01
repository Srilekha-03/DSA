# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        d=dict()
        curr=head
        while curr:
            if curr.val in d:
                d[curr.val]+=1
            else:
                d[curr.val]=1
            curr=curr.next
        dummy=ListNode(-1)
        mover=dummy
        for key,val in d.items():
            if val==1:
                mover.next=ListNode(key)
                mover=mover.next
        return dummy.next
