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
    n_stacks = 1         # default 2 common stacks
    _common_data = [0]
    _common_capacity = 128 * n_stacks   # default 128 bits capacity for common stack
    _stack_indexes = [0] * n_stacks

    def __init__(self, capacity: int = None, n_stacks: int = None):
        """capacity -> capacity of the normal stack.\n
           n_stacks -> number of stacks in the common stack.\n
           NOTE: Only use one of capacity or n_stacks init param
           at a time.\n"""

        if capacity:
            self.capacity = capacity
            self.data = []
        if n_stacks:
            Stack.n_stacks = n_stacks
            Stack._stack_indexes *= n_stacks
            Stack._common_data *= Stack._common_capacity

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

    # Common Stack functions
    def push_n(self, val: int, stack_no: int) -> bool:
        if stack_no > Stack.n_stacks or Stack.n_stacks <= 1:
            return False
        
        n_vals_stack = Stack._stack_indexes[stack_no - 1]
        val_pos = (n_vals_stack * Stack.n_stacks) + (stack_no - 1)

        if val_pos <= Stack._common_capacity:
            Stack._common_data[val_pos] = val
            Stack._stack_indexes[stack_no - 1] += 1
            return True
        
        return False

    def pop_n(stack_no: int) -> int:
        pass

    def peek_n(stack_no: int) -> int:
        pass

    def display_common_stack(no_of_stack: int) -> int:
        pass