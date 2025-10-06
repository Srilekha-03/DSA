# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        new_head=self.reverse(slow.next)
        slow.next=None
        i=head
        j=new_head
        while j:
            temp1=i.next
            temp2=j.next
            i.next=j
            j.next=temp1
            i=temp1
            j=temp2
        return head
    def reverse(self,root):
        prev=None
        cur=root
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        return prev



        """
        Do not return anything, modify head in-place instead.
        """
        