class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
        
    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = new

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        
    # def remove(self, index: int) -> bool:
    #     prev = self.head
    #     curr = prev.next
    #     i = 0
    #     while curr:
    #         if i == index:
    #             prev.next = curr.next
    #             curr = curr.next
    #             return True
    #         i +=1
    #         prev = prev.next
    #         curr = curr.next
    #     return False

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values


        
