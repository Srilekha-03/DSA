# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while True:
            count = 0
            temp = current

            # Check if there are at least k nodes to reverse
            while temp and count < k:
                temp = temp.next
                count += 1

            if count < k:
                break

            # Reverse k nodes
            nextGroup = current
            prevGroup = prev
            for _ in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # Connect the reversed group to the previous group
            prevGroup.next.next = current
            temp = prevGroup.next
            prevGroup.next = prev
            prev = temp

        return dummy.next


        

        
        
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        