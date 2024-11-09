# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        count = 0
        while fast:
            fast = fast.next
            count += 1
        if count%2==0:
            count = count/2
        else:
            count = count//2 
        while count:
            slow = slow.next
            count -=1
        return slow