#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def rotate(self, head, rotations):
    # TODO: Write your code here
    if head is None and head.next is None and rotations == 0:
      return head

    tail = head
    length = 1
    while tail.next is not None:
      tail = tail.next
      length += 1
    
    rotations %= length
    if rotations == 0:
      return head
    
    newTail = head
    for _ in range(length - rotations - 1):
      newTail = newTail.next
    
    newHead = newTail.next
    newTail.next = None
    tail.next = head
    return newHead
