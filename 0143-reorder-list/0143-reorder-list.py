# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        st = []
        curr = head
        while curr:
            st.append(curr)
            curr = curr.next

        k = len(st) // 2
        curr = head
        while k > 0:
            topNode = st.pop()
            temp = curr.next
            curr.next = topNode
            topNode.next = temp
            curr = temp
            k -= 1
        curr.next = None
        