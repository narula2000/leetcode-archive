# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSort(a, b):
            tmp = ListNode(0)
            head = tmp
            while a and b:
                if a.val < b.val:
                    tmp.next = ListNode(a.val)
                    tmp = tmp.next
                    a = a.next
                else:
                    tmp.next = ListNode(b.val)
                    tmp = tmp.next
                    b = b.next
            if not a:
                tmp.next = b
            else:
                tmp.next = a

            return head.next

        # Too slow ???
        # result = ListNode(float('-inf'))  
        # for lst in lists:
        #    result = mergeSort(result, lst)

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = mergeSort(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None