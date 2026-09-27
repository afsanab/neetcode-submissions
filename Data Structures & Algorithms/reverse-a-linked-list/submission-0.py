# Definition for singly-linked list.
# class ListNode:
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      curr = head.next
      head.next = None
      while curr:
        n = curr.next
        curr.next = head
        head = curr
        curr = n
      return head
