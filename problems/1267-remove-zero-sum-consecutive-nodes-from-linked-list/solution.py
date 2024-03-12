# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0, head)
        curr = tmp
        sum_prefix, dict_sums = 0, {}
        
        while curr:
            sum_prefix += curr.val
            dict_sums[sum_prefix] = curr
            curr = curr.next

        sum_prefix = 0
        curr = tmp

        while curr:
            sum_prefix += curr.val
            curr.next = dict_sums[sum_prefix].next
            curr = curr.next
        
        return tmp.next

