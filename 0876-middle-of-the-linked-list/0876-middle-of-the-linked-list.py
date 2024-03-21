# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        var = head
        while var:
            count+=1
            var = var.next
        count = count//2
        while head:
            if(count<=0):
                return head
            count-=1
            head= head.next        