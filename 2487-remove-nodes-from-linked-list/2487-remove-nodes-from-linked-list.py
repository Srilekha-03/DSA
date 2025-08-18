# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return self.helper(head)
    
    def helper(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        s = self.helper(head.next)
        head.next = None   # detach
        
        if head.val >= s.val:
            head.next = s
            return head
        return s