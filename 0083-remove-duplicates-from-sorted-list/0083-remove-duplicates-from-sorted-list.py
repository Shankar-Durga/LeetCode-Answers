# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return
        slow = head
        fast =head.next
        while fast:
            if slow.val==fast.val:
                fast=fast.next
                slow.next = slow.next.next
            else:
                slow = slow.next
                fast = fast.next
        return head