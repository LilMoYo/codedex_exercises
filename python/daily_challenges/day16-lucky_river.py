def lucky_river(river, hours):
    river_clover = []
    counter = 0
    
    for index, value in enumerate(river):
        if value == '☘️':
            river_clover.append(index)
            
    while counter < hours:
        counter += 1
        for _ in range(len(river)):
            for rc_index in river_clover:
                if rc_index+counter >= len(river):
                    break
                else:       
                    river[rc_index+counter] = '☘️'
        print(f'Counter: {counter}')
    return river
        
    
br_line = "--------------------------\n"


input1_river = ['💧', '☘️', '💧', '💧', '💧', '☘️', '💧', '💧']
input1_hours = 1

result1 = lucky_river(input1_river, input1_hours)
print(f"Output: {result1}")
print(br_line)


input2_river = ['☘️', '💧', '💧', '💧', '💧', '☘️', '💧', '💧']
input2_hours = 3

result2 = lucky_river(input2_river, input2_hours)
print(f"Output: {result2}")
print(br_line)
