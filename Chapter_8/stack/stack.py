# stack.py

# Stack class

class Stack:
    """
    Stack class implements a last in first out LIFO algorithm
    """

    def __init__(self, starting_stack_as_list: list = None):
        if starting_stack_as_list is None:
            self.data_list: list = []

        else:
            self.data_list: list = starting_stack_as_list[:]  # make a copy

    def push(self, item) -> None:
        self.data_list.append(item)

    def pop(self):
        if len(self.data_list) == 0:
            raise IndexError

        element = self.data_list.pop()

        return element

    def peek(self):
        # Retrieve the top item, without removing it
        item = self.data_list[-1]

        return item

    def get_size(self):
        n_elements: int = len(self.data_list)

        return n_elements

    def show(self):
        # Show the stack in a vertical orientation
        print("Stack is:")
        for value in reversed(self.data_list):
            print(f"    {value}")