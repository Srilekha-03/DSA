"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dup_head= Node(head.val)
        curr=head
        dcurr=dup_head
        hashmap={}
        hashmap[curr]=dcurr
        while curr.next:
            dcurr.next=Node(curr.next.val)
            curr=curr.next
            dcurr=dcurr.next
            hashmap[curr]=dcurr
        curr=head
        dcurr=dup_head
        while curr:
            dcurr.random = hashmap.get(curr.random)
            curr=curr.next
            dcurr=dcurr.next
        return dup_head



        