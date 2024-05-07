# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        curr, num = head, 0
        ans = tmp = ListNode()
        while curr:
            num = num * 10 + curr.val
            curr = curr.next
        if num == 0: return ListNode()

        num *= 2
        nums = []
        while num > 0:
            digit = num % 10
            num //= 10
            nums.append(digit)
        for num in reversed(nums):
            tmp.next = ListNode(num)
            tmp = tmp.next

        return ans.next
        
