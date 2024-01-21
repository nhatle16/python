def is_even(n):
    if n == 0:
        return True
    else:
        is_prev_even = is_even(n-1)
        is_this_even = not is_prev_even
    return is_this_even

print(is_even(5))