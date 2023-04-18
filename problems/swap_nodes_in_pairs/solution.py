# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # Base case if last element in link list
        if not head or not head.next:
            return head

        current = head
        next_node = head.next

        # Send rest of the node to swap and put the rest of the node behind the swaped node i.e. the current node
        current.next = self.swapPairs(next_node.next)
         # Swapping
        next_node.next = current

        return next_node

"""
class EditorialSolution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next
"""