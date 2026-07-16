"""
LRU cache implementation.

The principle of a least recently used cache is to
only keep the most recently used data in the cache
and purge the rest.

This has been implemented using a doubly-linked list
in this example.
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity    # Maximum capacity of the cache
        self.size = 0                # Current capacity of the cache
        self.head = None            # A pointer to the first node of the cache
        self.tail = None            # A pointer to the last node of the cache
        self.hash_map = {}          # Map to check if a val exists
 
    def put(self, val):
        # If val is present, make that respective Node the head node.
        val_node = self.hash_map.get(val)
        if val_node:
            self._move_to_front(val_node)
            return
        
        # val does not exist, insert it
        new_node = Node()
        new_node.data = val
        self._add_to_front(new_node)
        return

    def get(self, val) -> Node:
        node =  self.hash_map.get(val)

        # If node is None, return
        if node == None:
            return None

        # If node exists, move it to the front
        self._move_to_front(node)
        return node

    def display(self):
        "Display the list"
        curr = self.head
        while curr:
            print(curr.data, end='->')
            curr = curr.next
        print('None')

    def _move_to_front(self, node: Node):
        "Make an existing node the head node"
        # Return if node is already head
        if node == self.head:
            return

        # Swap adjacent nodes pointers
        node.prev.next = node.next
        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        # Move node to the front
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

        return

    def _add_to_front(self, node: Node):
        "Add the node as the head node"

        # Remove last node if cache is over capacity
        if self.size == self.capacity:
            old_tail = self.tail

            # point tail to its previous node
            self.tail = self.tail.prev          
            self.tail.next = None

            # remove entry from map
            del self.hash_map[old_tail.data]    
            
            # Remove data and previous pointer
            old_tail.prev = None
            old_tail.data = None

        # Configure length of the doubly linked list and the tail pointer
        else:
            self.size += 1

        # Add node and its val in the map
        self.hash_map[node.data] = node

        # Configure head and tail node if len equals 1
        if self.size == 1:
            self.head = node
            self.tail = node    # tail node will be the first node added to the list
        # Add given node at the front of the doubly-linked-list
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        return
      

if __name__ == '__main__':
    # The following reference sequence is to simulate
    # real-world data being processed by the cache.
    ref_seq = [10, 20, 10, 30, 40, 50, 30, 40, 60, 30]

    cache = LRUCache(4)    # Create cache with max capacity set to 4

    cache.put(10)
    cache.put(20)
    cache.put(10)
    cache.put(30)
    cache.put(40)
    cache.put(50)
    cache.put(30)
    cache.put(40)
    cache.put(60)
    cache.put(30)

    # Display the cache
    cache.display()

    # Fetch sample values from cache
    x = cache.get(40)
    if x:
        print(x.data)
    else:
        print('Not found!')

    # We read 40, it should've moved to front, lets display the cache
    cache.display()
