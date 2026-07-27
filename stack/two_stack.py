"""
This is the demonstration of the implementation of the
two stack feature of the my_stack module that utilizes
a common stack to store data of multiple stacks for better
efficiency.
"""

from my_stack import Stack

if __name__ == '__main__':
    common_stack = Stack(n_stacks=3)
    
    seq_stack1 = [2, 5, 8, 43, 22, 56]
    seq_stack2 = [32, 54, 21, 3]
    seq_stack3 = [44, 23, 95,34, 84]

    stack_no = 1
    for val in seq_stack1:
        common_stack.push_n(val, stack_no)

    stack_no = 2
    for val in seq_stack2:
        common_stack.push_n(val, stack_no)

    stack_no = 3
    for val in seq_stack3:
        common_stack.push_n(val, stack_no)

    print(common_stack._common_data)
