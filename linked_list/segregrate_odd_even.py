"""
Segregate odd and even values in a Linked List.

Time -> O(n)
Space -> O(1)
"""

from singly_linked_list import LinkedList

def segregate(ll: LinkedList):
    curr = ll.head

    # List Pointers
    os = oe = es = ee = None

    while curr != None:
        x = curr.data

        if x % 2 == 0:
            if es == None:
                es = ee = curr
            else:
                ee.next = curr
                ee = ee.next
        else:
            if os == None:
                os = oe = curr
            else:
                oe.next = curr
                oe = oe.next

        curr = curr.next
    
    if os == None or es == None:
        return ll.head
    
    oe.next = es
    ee.next = None

    ll.head = os


if __name__ == '__main__':
    list1 = LinkedList()
    list1.init(1, 11)

    segregate(list1)
    list1.display()
