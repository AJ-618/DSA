"""
Find the intersection point of two linked lists.

Time -> O(m + n) where m and n are respective linked list sizes.
Space -> O(1)
"""

from singly_linked_list import LinkedList, Node

def intersection(l1: LinkedList, l2: LinkedList) -> Node:
    h1 = l1.head
    h2 = l2.head

    c1 = l1.count()
    c2 = l2.count()

    diff = abs(c1 - c2)

    if c1 > c2:
        for i in range(diff):
            h1 = h1.next
    else:
        for i in range(diff):
            h2 = h2.next

    while h1 != None:
        if h1 == h2:
            return h1
        else:
            h1 = h1.next
            h2 = h2.next

    return None

if __name__ == '__main__':
    l1 = LinkedList()
    l1.init(1, 11)

    int_node = l1.get_node(7)

    l2 = LinkedList()
    l2.init(4, 11)

    l2.tail.next = int_node

    int1 = intersection(l1, l2)
    if int1:
        print("Intersection found at:", int1.data)
    else:
        print("No intersection found!")
