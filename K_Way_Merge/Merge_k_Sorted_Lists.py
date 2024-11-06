# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap =[(root.val, i, root) for i, root in enumerate(lists) if root]
        heapq.heapify(minHeap)
        head = ListNode(0)
        tail = head
        while minHeap:
            v, i, node = heappop(minHeap)
            tail.next = node
            tail = tail.next
            if node.next is not None:
                heappush(minHeap, (node.next.val, i, node.next))
        return head.next