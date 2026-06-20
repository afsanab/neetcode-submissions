# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#my initial solution
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         indexes = {}
#         temp = head
#         index = 0
#         while temp:
#             if temp in indexes:
#                 index = indexes[temp]
#                 return True
#             else:
#                 indexes[temp] = index
#                 temp = temp.next
#                 index +=1
#         index = -1
#         return False


#neetcodes solution, with O(1) memory, and same runtime - O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #initialize both slow and fast to head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # at any point
                return True
        return False # if fast or fast.next ever get to NULL