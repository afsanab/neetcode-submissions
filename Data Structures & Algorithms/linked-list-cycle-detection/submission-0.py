# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        indexes = {}
        temp = head
        index = 0
        while temp:
            if temp in indexes:
                index = indexes[temp]
                return True
            else:
                indexes[temp] = index
                temp = temp.next
                index +=1
        index = -1
        return False