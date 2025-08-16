# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap={}
        prefix=0
        dummynode=ListNode(0)
        dummynode.next=head
        hashmap[0]=dummynode
        while head:
            prefix+=head.val
            if prefix in hashmap:
                start=hashmap[prefix]
                temp=start
                psum=prefix
                while temp!=head:
                    temp=temp.next
                    psum+=temp.val
                    if temp!=head:
                        del hashmap[psum]
                start.next=head.next
            else:
                hashmap[prefix]=head
            head=head.next
        return dummynode.next



        