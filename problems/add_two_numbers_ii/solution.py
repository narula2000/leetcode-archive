# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return
        
        l1_val = 0
        while l1:
            l1_val = l1_val * 10 + l1.val
            l1 = l1.next

        l2_val = 0
        while l2:
            l2_val = l2_val * 10 + l2.val
            l2 = l2.next
        

        l_sum = l1_val + l2_val

        result = ListNode()
        curr = result
        for char in str(l_sum):
            curr.next = ListNode(int(char))
            curr = curr.next
        
        return result.next