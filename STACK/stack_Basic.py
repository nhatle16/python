from collections import deque

# Implementation of stack using deque
class Stack:
    def __init__(self):
        self.stack = deque()
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Can't pop from an empty stack!")
        
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Top of an empty stack DNE!")
        
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print("Stack: ", list(self.stack))
    
# Implementation of stack using a list
class Stack2:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Can't pop from an empty stack!")
        
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Top of an empty stack DNE!")
        
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print("Stack: ", self.stack)
    
if __name__ == "__main__":
    # Create an instantiation of Stack class
    myStack = Stack2()

    myStack.push(1)
    myStack.push(6)
    myStack.push(0)
    myStack.push(6)
    myStack.print_stack()
    print(myStack.pop())
    myStack.print_stack()
    print(myStack.top())
    print(myStack.size())
    print(myStack.is_empty())