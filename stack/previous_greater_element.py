"""
Given an array of distinct integer, find closest (position-wise) greater
on left of every element. If there is no greater element on left, then print
-1.

i/p: [15, 10, 18, 12, 4, 6, 2, 8]
o/p: -1, 15, -1, 18, 12, 12, 6, 12

Time Complexity -> O(n)
Space Complexity -> O(n), O(1) if printing output
"""

from my_stack import Stack

def previous_greater_element(arr: list[int]) -> list[int]:
    stack = Stack(capacity=((len(arr)+2)))
    res = [-1]
    stack.push(arr[0])

    for i in range(1, len(arr)):
        while stack.is_empty() == False and stack.peek() <= arr[i]:
            stack.pop()

        res.append(-1) if stack.is_empty() else res.append(stack.peek())
        stack.push(arr[i])

    return res


if __name__ == '__main__':
    arr1 = [20, 30, 10, 5, 15]
    print(previous_greater_element(arr1))       # -1, -1, 30, 10, 30

    arr2 = [15, 10, 18, 12, 4, 6, 2, 8]
    print(previous_greater_element(arr2))       # -1, 15, -1, 18, 12, 12, 6, 12
