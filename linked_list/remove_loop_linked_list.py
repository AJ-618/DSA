"""
Remove the loop from a circular linked list.
Do this so by making the last node point to
None.
"""

from singly_linked_list import LinkedList

if __name__ == '__main__':
    list1 = LinkedList()
    list1.init(1, 7)
    list1.display()
    LinkedList.create_circular_list(list1)

    LinkedList.detect_remove_loop(list1)

    list1.display()
