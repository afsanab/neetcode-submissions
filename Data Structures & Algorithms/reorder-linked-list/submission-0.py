# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head.next
        #split them
        while l1 and l1.next and l1.next.next and l1.next.next.next:
            #next 
            nxt = l1.next
            l1.next = nxt.next
            #next next
            nxt2 = nxt.next
            nxt.next = nxt2.next
        #reverse second
        prev = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            curr = nxt
            prev = curr
        l2 = prev
        #merge
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2

        
        
        

        
        