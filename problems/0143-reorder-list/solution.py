# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return []

        slow, fast = head, head

        while fast.next and fast.next.next: # Find the mid
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        while curr: # Reverse last half
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = None

        head1, head2 = head, prev
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next
