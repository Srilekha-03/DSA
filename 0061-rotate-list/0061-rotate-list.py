# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length=0
        curr=head
        while curr:
            curr=curr.next
            length+=1
        k=k%length
        if k==0:
            return head
        new_head=self.reverse(head)
        curr2=new_head
        while k>1:
            curr2=curr2.next
            k-=1
        second_half=curr2.next
        curr2.next=None
        first_half=new_head
        x=self.reverse(first_half)
        y=self.reverse(second_half)
        curr3=x
        while curr3.next:
            curr3=curr3.next
        curr3.next=y
        return x

    def reverse(self,head):
        if not head or not head.next:
            return head
        new_head=self.reverse(head.next)
        head.next.next=head
        head.next=None
        return new_head