def recamanSequence(n, sequence, seen, cur):
    if n == 0:
        return sequence
    else:
        prev = sequence[-1] if sequence else 0
        next_num = prev - cur
        if next_num < 0 or next_num in seen:
            next_num = prev + cur
        seen.add(next_num)
        sequence.append(next_num)
        return recamanSequence(n-1, sequence, seen, cur+1)
        
if __name__ == "__main__":
    # n = int(input("Enter number: ")) 
    num = 7   
    res = recamanSequence(num, [], set(), 0)
    print(res)