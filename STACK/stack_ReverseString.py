from stack_Basic import Stack

def reverse_str(s):
    st = Stack()
    res = ""
    
    for char in s:
        st.push(char)
        
    while not st.is_empty():
        res += st.pop()
        
    return res

if __name__ == "__main__":
    s = input("Enter a string: ")
    ans = reverse_str(s)
    
    print(ans)    