# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        dummy = ans  
        while l1 or l2: #check is each linkedlist None or not and breaks
            current = 0
            if l1:
                current += l1.val
                l1 = l1.next
            if l2:
                current += l2.val
                l2 = l2.next
            dummy.next = ListNode(current%10)
            dummy = dummy.next
            if current >9:
                if l1:
                    l1.val +=1
                elif l2:
                    l2.val+=1
                else:
                    dummy.next = ListNode(1)
                    dummy = dummy.next
        return ans.next

         