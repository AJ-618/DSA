"""
Balanced Parenthesis

Time -> O(n)
Space -> O(n)
"""

from my_stack import Stack

def is_parenthesis_balanced(seq: list) -> bool:
    # Create stack of size 10
    stack = Stack(10)

    for bracket in seq:
        if bracket == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                return False
        elif bracket == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                return False
        elif bracket == '}':
            if stack.peek() == '{':
                stack.pop()
            else:
                return False
        else:
            stack.push(bracket)
    
    if stack.data:
        return False

    return True

if __name__ == '__main__':
    seq1 = ['(', '[', '{', '}', ']', ')']
    seq2 = ['(', '[', ')']
    seq3 = ['(', '{', '}']
    seq4 = [')', '(', ')']
    seq5 = ['{', '}', '(', '[', ']', ')']

    print('seq1', seq1, is_parenthesis_balanced(seq1))
    print('seq2', seq2, is_parenthesis_balanced(seq2))
    print('seq3', seq3, is_parenthesis_balanced(seq3))
    print('seq4', seq4, is_parenthesis_balanced(seq4))
    print('seq5', seq5, is_parenthesis_balanced(seq5))
