"""
Largest rectangular area histogram

i/p: [6, 2, 5, 4, 1, 5, 6]
o/p: 10
"""

from my_stack import Stack

def get_max_area(arr: list[int]) -> int:
    stack = Stack(8)
    res = 0
    n = len(arr)

    for i in range(n):
        while not stack.is_empty() and arr[stack.peek()] >= arr[i]:
            top = stack.pop()
            curr = arr[top] * (i if stack.is_empty() else (i - stack.peek() - 1))
            res = max(res, curr)

        stack.push(i)

    while not stack.is_empty():
        top = stack.pop()
        curr = arr[top] * (n if stack.is_empty() else (n - stack.peek() - 1))
        res = max(res, curr)

    return res


if __name__ == '__main__':
    arr1 = [6, 2, 5, 4, 1, 5, 6]
    print(get_max_area(arr1))
