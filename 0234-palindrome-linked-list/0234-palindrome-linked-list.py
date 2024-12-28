# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head 
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        newNode=self.reverse(slow.next)
        first=head
        second=newNode
        while second!=None:
            if first.val!=second.val:
                self.reverse(newNode)
                return False
            first=first.next
            second=second.next
        self.reverse(newNode)
        return True
    def reverse(self,head):
        prev=None
        temp=head
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev       

        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        