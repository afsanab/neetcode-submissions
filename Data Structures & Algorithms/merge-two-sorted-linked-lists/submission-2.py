# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        newHead = ListNode()
        temp = newHead

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        #once one of the lists are NULL, you have to add whats left of the other to
        #the newHead, if both are NULL then your done
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        #.next beacuse the first node "newHead is empty, and just used at a pointer
        return newHead.next
