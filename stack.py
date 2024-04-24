class Stack:
    def __init__(self):
        self.my_stack = []

    def push(self, item):
        self.my_stack.append(item)

    def peek(self):
        return self.my_stack[-1]

    def isEmpty(self):
        return self.my_stack == []

    def viewItems(self):
        return self.my_stack[::-1]

    def popItem(self):
        return self.my_stack.pop()
