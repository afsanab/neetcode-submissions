# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        nxt1 = list1.next
        nxt2 = list2.next
        if list1.val < list2.val or list1.val == list2.val:
            head = list1
            list1.next = list2
            list1 = nxt1
            nxt1 = nxt1.next
        else:
            list2.next = list1
            list2 = nxt2
            nxt2 = nxt2.next
        while nxt1 and nxt2:
            if list1.val < list2.val or list1.val == list2.val:
                list1.next = list2
                list1 = nxt1
                nxt1 = nxt1.next
            elif list2.val < list1.val:
                list2.next = list1
                list2 = nxt2
                nxt2 = nxt2.next
        return head
            
                
                

