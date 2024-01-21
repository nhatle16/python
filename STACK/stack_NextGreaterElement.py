from stack_Basic import Stack2

def next_greater(nums):
    st = Stack2()
    res = [-1] * len(nums)
    
    for i in range(len(nums)):
        while not st.is_empty() and nums[i] > nums[st.top()]:
            # Use pop() instead of top() to remove the index
            # from the stack after NGE has been found
            res[st.pop()] = nums[i] 

        st.push(i)
        
    return res

if __name__ == "__main__":
    my_list = []
    num_ele = int(input("Input length: "))
    
    for _ in range(num_ele):
        value = int(input("Enter a number: "))
        my_list.append(value)  
                
    print(next_greater(my_list))