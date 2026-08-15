"""
Stock span problem.

Find the number of consecutive days in the provided array
where the value to the left is smaller or equal to the current
value.

IDEA: Store index of previous big element in stack.

NOTE: Good Problem.
"""

from my_stack import Stack

def span(arr: list[int]) -> dict:
    stack = Stack(20)
    stack.push(0)
    print(1)

    for i in range(1, len(arr)):
        while stack.is_empty() == False and arr[stack.peek()] <= arr[i]:
            stack.pop()

        span = i if stack.is_empty() else i - stack.pop()
        print(span)

        stack.push(i)


if __name__ == '__main__':
    arr1 = [18, 12, 13, 14, 11, 16]
    span(arr1)
