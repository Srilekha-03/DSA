# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        mid = self.getMiddle(head)
        right = mid.next
        mid.next = None
        
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)
        
        return self.merge(left_sorted, right_sorted)
    
    def getMiddle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        