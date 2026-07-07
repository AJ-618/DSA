"""
This algorithm is used to detect loops inside
a Linked List. While doing so it does not
modify the structure of the linked list.

The main idea here is that we make use of two pointers
i.e. the slow and the fast pointer. If the list is
circular, both of them will meet at somepoint together.

If the list is not circular, the pointers will reach None.

Time -> O(n)
Space -> O(1)
"""

import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Importing from parent dir, thus the warning
from linked_list.singly_linked_list import LinkedList

if __name__ == '__main__':
    list1 = LinkedList()
    list1.init(1, 7)

    LinkedList.create_circular_list(list1)

    print(LinkedList.is_list_circular(list1))
