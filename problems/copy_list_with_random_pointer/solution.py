"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]', seen={None: None}) -> 'Optional[Node]':
        if head not in seen:
            seen[head] = Node(head.val)
            seen[head].next = self.copyRandomList(head.next, seen)
            seen[head].random = self.copyRandomList(head.random, seen)
        return seen[head]