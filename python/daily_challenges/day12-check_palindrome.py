def check_palindrome(sequence):
    sequence = sequence.lower()
    sequence = sequence.replace(" ", "")
    print(sequence)
    
    rev_sequence = sequence[::-1]
    print(rev_sequence)
    
    if sequence == rev_sequence:
        return True
    
    else:
        return False
    
br_line = "--------------------------\n"


input1 = "racecar"

result1 = check_palindrome(input1)
print(f"Output: {result1}")
print(br_line)


input2 = "Was it a car or a cat I saw"

result2 = check_palindrome(input2)
print(f"Output: {result2}")
print(br_line)


input3 = "11 11"

result3 = check_palindrome(input3)
print(f"Output: {result3}")
print(br_line)


input4 = "12345"

result4 = check_palindrome(input4)
print(f"Output: {result4}")
print(br_line)
