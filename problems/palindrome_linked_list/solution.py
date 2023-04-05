# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head
        
        def helper(node):
            if node:
                if not helper(node.next):
                    return False
                if node.val != self.front.val:
                    return False
                self.front = self.front.next
            return True

        return helper(head)