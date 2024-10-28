# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current is not None:
            while stack and current.val > stack[-1].val:
                stack.pop()
            if stack:
                stack[-1].next = current
            stack.append(current)
            current = current.next
        return stack[0]