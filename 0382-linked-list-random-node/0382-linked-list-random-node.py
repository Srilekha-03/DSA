# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.arr=[]
        self.length=0
        temp=head
        while temp:
            self.length+=1
            self.arr.append(temp.val)
            temp=temp.next  

    def getRandom(self) -> int:
        index=random.randint(0,self.length-1)
        return self.arr[index]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()