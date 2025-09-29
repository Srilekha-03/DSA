# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        c=1
        prev=None
        while c<left:
            prev=curr
            curr=curr.next
            c+=1
        rev1=curr
        while c<right:
            curr=curr.next
            c+=1
        last=curr.next
        curr.next=None
        new_head=self.reverse(rev1)
        if prev:
            prev.next=new_head
        rev1.next=last
        return head if prev else new_head
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        return prev

        


        