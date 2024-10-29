# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head
        dummy = head.next
        while dummy:
            temp.val, dummy.val = dummy.val,temp.val
            
            if not dummy.next: 
                break
                
            temp = temp.next.next
            dummy = dummy.next.next
            
            
        return head