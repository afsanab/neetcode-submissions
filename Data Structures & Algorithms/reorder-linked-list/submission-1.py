# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split list? or find middle - fast and slow pointer
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second part of list
        #from slow.next --> fast - reverse the list
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        #merge them
        # head - prev
        while head and prev:
            tmp = head.next
            head.next = prev
            head = tmp
            tmp2 = prev.next
            prev.next = head
            prev = tmp2
        
        

        