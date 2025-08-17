# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next

        k1=k
        k2=n-k+1
        temp1=head
        temp2=head
        while k1>1:
            temp1=temp1.next
            k1-=1
        while k2>1:
            temp2=temp2.next
            k2-=1
        temp1.val,temp2.val=temp2.val,temp1.val
        return head



        