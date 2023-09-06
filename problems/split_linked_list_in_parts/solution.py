# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k

        ll_len = 0
        node = root
        while node:
            ll_len += 1
            node = node.next

        num, remain = divmod(ll_len, k)

        node = root
        prev = None

        for i in range(k):
            res[i] = node
            for j in range(num + (1 if remain > 0 else 0)):
                prev = node
                node = node.next
            
            if prev:
                prev.next = None
            
            if remain > 0:
                remain -= 1
        
        return res