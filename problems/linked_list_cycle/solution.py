# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next: # End of the Linked List
                return False
            
            slow, fast = slow.next, fast.next.next
        
        return True
