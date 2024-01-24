from typing import Optional

class Solution:
    # Define the method hasCycle with one parameter 'head'.
    # The 'Optional' type hint suggests that 'head' can be either of a ListNode type or None.
    def hasCycle(self, head: Optional) -> bool:
        # Initialize two pointers, slow_pointer and fast_pointer, both starting at 'head'.
        slow_pointer = head
        fast_pointer = head

        # Continue looping as long as fast_pointer and fast_pointer.next are not None.
        # This check ensures that we don't access a next attribute of a None object, which would raise an AttributeError.
        while fast_pointer and fast_pointer.next:
            # Move slow_pointer one step forward.
            slow_pointer = slow_pointer.next
            # Move fast_pointer two steps forward.
            fast_pointer = fast_pointer.next.next

            # Check if the two pointers meet (point to the same node).
            # If they do, there is a cycle in the linked list.
            if slow_pointer == fast_pointer:
                return True

        # If the loop exits, it means fast_pointer has reached the end of the linked list (i.e., no cycle).
        return False
