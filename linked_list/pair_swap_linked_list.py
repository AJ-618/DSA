"""
Swap the pair of nodes inside a linked list.

Time -> O(n)
Space -> O(1)
"""

from singly_linked_list import LinkedList

def swap(ll: LinkedList):
    curr = ll.head
    first_swap = False
    prev_node = None

    while curr != None:
        if curr.next == None:
            break
        
        next_node = curr.next

        if first_swap == False:
            ll.head = next_node
            first_swap = True

        if prev_node:
            prev_node.next = next_node

        curr.next = next_node.next
        next_node.next = curr

        prev_node = curr
        curr = curr.next


if __name__ == '__main__':
    l1 = LinkedList()
    l1.init(1, 10)
    l1.display()

    swap(l1)

    l1.display()
