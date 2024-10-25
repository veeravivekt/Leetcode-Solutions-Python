# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second is not None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first = head
        second = prev
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True