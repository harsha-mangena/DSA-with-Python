class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prv=None
        while(current):
            nxt=current.next
            current.next=prv
            prv=current
            current=nxt
        return prv
