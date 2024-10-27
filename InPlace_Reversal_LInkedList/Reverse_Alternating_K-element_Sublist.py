#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def reverse(self, head, k):
    # TODO: Write your code here
    prev, current = None, head
    while current is not None:
      i = 0
      lastnode_previous = prev
      lastnode_subarray = current
      while current is not None and i < k:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        i += 1
      
      if lastnode_previous is not None:
        lastnode_previous.next = prev
      else:
        head = prev
      
      lastnode_subarray.next = current
      i = 0
      while current is not None and i < k:
        prev = current
        current = current.next
        i += 1

    return head