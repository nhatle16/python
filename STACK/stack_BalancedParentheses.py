from stack_Basic import Stack2

def is_balanced(expression):
    mystack = Stack2()
    
    opening = {'(', '{', '['}
    closing = {')': '(', '}': '{', ']': '['}
    
    for symbol in expression:
        # Add opening parentheses to stack
        if symbol in opening:
            mystack.push(symbol)
            
        elif symbol in closing:
            # Check if the last opening parenthesis match
            # with the corresponding of closing parenthesis
            if not mystack or mystack.pop() != closing[symbol]:
                return False
            
    print(mystack.stack)
    
    return not mystack.stack
    
if __name__ == "__main__":
    expression = input("Enter an expression: ")
    print(is_balanced(expression))