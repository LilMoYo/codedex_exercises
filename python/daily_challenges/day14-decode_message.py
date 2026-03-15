def decode_message(message, shift):
    message_lower = message.lower()
    print(message_lower)
    ascii_message = message_lower.encode('ascii')
    print(list(ascii_message))
    
    enc_byte = []
    temp_char = 0
    
    if shift > 26:
        shift = shift % 26
    
    for char in ascii_message:
        temp_char = char - shift
        if temp_char <= 47:
            enc_byte.append(char)
            print(char)
        elif temp_char >= 97 and temp_char <= 122:
            enc_byte.append(temp_char)
            print(temp_char) 
        else:
            temp_char = 122 - (96 - temp_char)
            print(f'temp_char: {temp_char}')
            enc_byte.append(temp_char)

            
    print(enc_byte)
    enc_message_list = list(map(chr, enc_byte))
    enc_message = ''.join(enc_message_list)
    return enc_message
    
br_line = "--------------------------\n"


input1_message = "dwwdfn dw gdzq"
input1_shift = 3

result1 = decode_message(input1_message, input1_shift)
print(f"Output: {result1}")
print(br_line)


input2_message = "ymj bfqwzx bfx ufzq"
input2_shift = 5

result2 = decode_message(input2_message, input2_shift)
print(f"Output: {result2}")
print(br_line)


input3_message = "ai wlsyph womt kcq gpeww"
input3_shift = 4

result3 = decode_message(input3_message, input3_shift)
print(f"Output: {result3}")
print(br_line)


input4_message = "xli ribx hempc gleppirki mw efsyx xli swgevw"
input4_shift = 30

result4 = decode_message(input4_message, input4_shift)
print(f"Output: {result4}")
print(br_line)