# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = ""
        p1 = l1
        p2 = l2
        ans = 0
        sample = l1
        while p1 or p2:
            if p1:
                a = str(p1.val)+a
                p1 = p1.next
            if p2:
                b= str(p2.val)+b            
                p2 = p2.next
        ans = int(a)+int(b)
        while sample:
                sample.val = ans%10
                ans = ans//10
                if(ans!=0 and sample.next==None):
                    sample.next = ListNode(0)
                sample = sample.next
                

        return l1
        