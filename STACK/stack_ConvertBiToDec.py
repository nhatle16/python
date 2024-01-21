from stack_Basic import Stack2

def converter(bi_str):
    st = Stack2()
    count, dec = 0, 0
    
    for i in bi_str:
        st.push(i)
    
    while count < len(bi_str):    
        dec += int(st.pop()) * pow(2, count)
        count += 1
    
    return dec
    
if __name__ == "__main__":
    s = input("Type in a str: ")
    res = converter(s)
    print(res)