# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        firstPointer = head
        secondPointer = None
        thirdPointer = None
        while firstPointer != None:
            secondPointer = firstPointer
            firstPointer = firstPointer.next
            secondPointer.next = thirdPointer
            thirdPointer = secondPointer
        
        head = secondPointer
        return head
        