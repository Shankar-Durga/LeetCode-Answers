class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(temp):
            prev = None
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            return prev
        
        rev = reverse(head)
        carry = 0
        res = ListNode(-1)
        ptr = rev
        cur = res
        while ptr or carry:
            val = ptr.val if ptr else 0
            temp = val+val+carry
            s = temp%10
            carry = temp//10
            newNode = ListNode(s)
            cur.next = newNode
            cur = cur.next
            ptr = ptr.next if ptr else None
        return reverse(res.next)