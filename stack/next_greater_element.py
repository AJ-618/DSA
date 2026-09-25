"""
NEXT GREATER ELEMENT

i/p: [5, 15, 10, 8, 6, 12, 9, 18]
o/p: 15, 18, 12, 12, 12, 18, 18, -1
"""

from my_stack import Stack

def next_greater_element(arr: list[int], n: int):
    # Output in reverse order

    stack = Stack(n + 2)
    stack.push(arr[n - 1])

    print("Output in reverse order")
    print(-1)

    for i in range(n - 2, -1, -1):
        while stack.is_empty() == False and stack.peek() <= arr[i]:
            stack.pop()

        next_greater = -1 if stack.is_empty() else stack.peek()
        print(next_greater, " ")
        stack.push(arr[i])


if __name__ == '__main__':
    arr1 = [5, 15, 10, 8, 6, 12, 9, 18]
    next_greater_element(arr1, 8)
