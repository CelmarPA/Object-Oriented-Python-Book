# main_stack_test.py

# Test code for basic push and pop on a stack

from stack import *


o_stack: Stack = Stack()
o_stack.push(5)
o_stack.push(12)
o_stack.push('Some data')
o_stack.push('Some more data')
o_stack.push(True)
o_stack.show()

while True:
    print()
    item = o_stack.pop()
    print(f"Next value from the stack is: {item}")
    if o_stack.get_size() == 0:
        break

    o_stack.show()

print("Stack is empty")
