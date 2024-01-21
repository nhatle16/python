from stack_Basic import Stack

def calculator(ope1, ope2, operator):
    if operator == '+':
        return ope1 + ope2
    elif operator == '-':
        return ope1 - ope2
    elif operator == '*':
        return ope1 * ope2
    elif operator == '/':
        return ope1 / ope2
    
def postfix_evaluate(s):
    st = Stack()
    
    for char in s:
        # Add to stack if it is a digit
        if char.isdigit():
            # Convert type str to int
            st.push(int(char))
            
        else:
            # Call the 2 operands
            operand1 = st.pop()
            operand2 = st.pop()
            # Calculate the expression
            res = calculator(operand1, operand2, char)
            st.push(res)
            
    return st.pop()
    
if __name__ == "__main__":
    s = input("Enter an expression: ")
    
    result = postfix_evaluate(s)
    print(result)    