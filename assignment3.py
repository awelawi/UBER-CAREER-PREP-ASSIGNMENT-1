from array import array
from ctypes import sizeof


class Stack:
    """Write a stack class that has the following operations:
    1. Pop, adds a new element to the array from the top where if n = len(array)
    Then n+1  = len(newArr)
    2. Pushes off the first element in the array from the top. Where if n = len(array)
    , then n-1  = len(newArr)"""

# Here is a sample execution trace:
# myStack = Stack()
# myStack.push(42)
# print “Top of stack: ”, myStack.top()
# # prints “Top of stack: 42”
# print “Size of stack: ”, myStack.size()
# # prints “Size of stack: 1”
# popped_value = myStack.pop()

    def __init__(self) -> None:
        return array
    
    def pop(self, x):
        return x.re

    def push(self, arr, y):
         len(arr) = len(arr) + 1
         arr[-1] = y
         return arr[-1]
    def size(self, arr
    ):
        return sizeof(arr)

    def isEmpty(self, arr):
        return arr.size() == 0
