# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        prev=None
        while node.next:
            node.val=node.next.val
            prev=node
            node=node.next
        prev.next=None
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        