"""
Remove duplicate elemenets from a sorted linked
list.
"""

from singly_linked_list import LinkedList

def remove_dups(ll: LinkedList):
    current = ll.head
    x = current
    while current:
        if current.data != x.data:
            x.next = current
            x = current
        current = current.next

    x.next = None


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(10)
    list1.append(10)
    list1.append(20)
    list1.append(20)
    list1.append(30)
    list1.append(30)
    list1.append(30)

    list1.display()

    remove_dups(list1)

    list1.display()
