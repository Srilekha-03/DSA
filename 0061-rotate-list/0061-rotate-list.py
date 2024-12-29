# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k %= length
        if k == 0:
            return head
        
        tail.next = head
        
        new_tail_position = length - k - 1
        new_tail = head
        for _ in range(new_tail_position):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        new_tail.next = None
        
        return new_head

  
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        