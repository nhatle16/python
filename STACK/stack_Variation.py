from stack_Basic import Stack2

def change_order(stack):
    stack2 = Stack2()
    
    while stack.size() > 1:
        stack2.push(stack.pop())
        
    bottom_value = stack.pop()
    
    while not stack2.is_empty():
        stack.push(stack2.pop())
        
    stack.push(bottom_value)
        
    return stack.stack
    
if __name__ == "__main__":
    lis = [23, 9, 17, 4]
    st = Stack2()
    for i in lis:
        st.push(i)
    
    res = change_order(st)
    
    print(res)