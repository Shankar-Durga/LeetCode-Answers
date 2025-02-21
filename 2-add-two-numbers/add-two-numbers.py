# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        sample = dummy
        while l1 or l2: # loop until both linkedlist react end
            value = 0
            if l1:
                value+=l1.val
                l1 = l1.next
            if l2:
                value+=l2.val
                l2 = l2.next
            sample.next = ListNode(value%10)
            sample = sample.next
            if value>9:
                if l1:
                    l1.val+=1
                elif l2:
                    l2.val+=1
                else:
                    sample.next = ListNode(1)   
        
        return dummy.next