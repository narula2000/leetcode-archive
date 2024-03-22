# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def helper(node):
            if not node:
                return True
            answer = helper(node.next) and node.val == self.tmp.val
            self.tmp = self.tmp.next
            return answer
        
        self.tmp = head
        return helper(head)
