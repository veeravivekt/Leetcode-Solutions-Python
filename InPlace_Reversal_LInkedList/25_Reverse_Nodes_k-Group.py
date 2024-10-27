# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        counterptr = head
        while counterptr is not None:
            counterptr = counterptr.next
            count += 1
        count = count // k

        prev, current = None, head
        while count > 0:
            lastnode_previous = prev
            lastnode_swapped = current
            i = 0
            while current is not None and i < k:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                i += 1
            count -= 1
            
            if lastnode_previous is not None:
                lastnode_previous.next = prev
            else:
                head = prev
            
            lastnode_swapped.next = current
            if current is None:
                break
            prev = lastnode_swapped
        return head