# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, current = None, head
        i = 0
        while current is not None and i < left - 1:
            prev = current
            current = current.next
            i += 1
        
        lastnode_unswapped = prev
        lastnode_swapped = current
        i = 0
        while current is not None and i < right - left + 1:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i += 1
        
        if lastnode_unswapped is not None:
            lastnode_unswapped.next = prev
        else:
            head = prev
        lastnode_swapped.next = current
        return head