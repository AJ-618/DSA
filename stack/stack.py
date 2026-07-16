"""
Stack implementation.

Stack is useful when we want data to be processed
in Last In, First Out (LIFO) order.

Applications of stack

1. Function calls
2. Balanced parenthesis
3. Reversing items
4. Undo/Redo, Forward/Backward (browser)
5. Infix to postfix/prefix
"""

class Stack:
    def __init__(self, capacity: int):
        self.data = []
        self.capacity = capacity

    def push(self, val: int) -> bool:
        if len(self.data) >= self.capacity:
            return False
        
        self.data.append(val)
        return True

    def pop(self) -> int:
        if self.data:
            return self.data.pop()
        else:
            return None

    def peek(self) -> int:
        if len(self.data):
            return self.data[-1]
        else:
            return None
