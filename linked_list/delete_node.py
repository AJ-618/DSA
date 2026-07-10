"""
Remove a node from a Linked List with a pointer
given to it.
"""

from singly_linked_list import LinkedList

if __name__ == '__main__':
    list1 = LinkedList()
    list1.init(1, 6)

    list1.display()

    node = list1.get_node(3)
    list1.remove_node(node)

    list1.display()
