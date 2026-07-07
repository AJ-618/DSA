"""
Custom python linked list implementation.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_circular_list(ll: LinkedList):
        curr = ll.head
        x = curr.next
        
        while curr.next != None:
            curr = curr.next

        curr.next = x

    def is_list_circular(ll: LinkedList) -> bool:
        slow = ll.head
        fast = ll.head

        while fast is not None:
            slow = slow.next

            if fast.next is not None:
                fast = fast.next.next
            else:
                return False

            if slow == fast:
                return True
            
        return False

    def init(self, s: int, e: int):
        while s < e:
            self.append(s)
            s += 1

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print("None")

