"""
Reverse a linked list in groups of 'n'.

Time -> O(n)
Space -> O(1)

NOTE: Good Problem
"""

from singly_linked_list import LinkedList

def reverse_n(ll: LinkedList, n: int):
    if ll is None or ll.head is None or n <= 1:
        return ll

    curr = ll.head
    prev_first = None
    is_first_pass = True

    while curr is not None:
        first = curr
        prev = None
        count = 0

        # Reverse n nodes
        while curr is not None and count < n:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        # 15 21 h32 pf40 p54

        # Update the head after reversing the first group
        if is_first_pass:
            ll.head = prev
            is_first_pass = False
        else:
            prev_first.next = prev

        # Connect the tail of the reversed group
        first.next = curr

        # Remember the tail of the current reversed group
        prev_first = first

    return ll


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)

    list1.display()

    reverse_n(list1, 3)

    list1.display()
