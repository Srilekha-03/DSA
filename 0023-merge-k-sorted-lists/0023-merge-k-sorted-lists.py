# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        if n==0:
            return None
        return self.partitionAndMerge(0,n-1,lists)
    def partitionAndMerge(self,start,end,lists):
        if start==end:
            return lists[start]
        mid=start+(end-start)//2
        left=self.partitionAndMerge(start,mid,lists)
        right=self.partitionAndMerge(mid+1,end,lists)
        return self.Merge(left,right,lists)
        
    def Merge(self,left,right,lists):
        if not left:
            return right
        if not right:
            return left
        if left.val<=right.val:
            left.next=self.Merge(left.next,right,lists)
            return left
        else:
            right.next=self.Merge(left,right.next,lists)
            return right
        return None


        