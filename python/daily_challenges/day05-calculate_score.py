def calculate_score(elements):
    elements_score = []
    
    for score in elements:
        goe_list = list(score[2])
        base_value = score[1]
        
        lowest_goe = min(goe_list)
        highest_goe = max(goe_list)
        
        goe_list.remove(lowest_goe)
        goe_list.remove(highest_goe)
        print(f"Lowest GOE: {lowest_goe},\n Highest GOE: {highest_goe},\n Score: {goe_list}")
        
        average_goe = sum(goe_list) / len(goe_list)
        print(f"Average GOE: {average_goe}")
        
        temp_goe = average_goe * 0.1 * base_value
        temp_score = base_value + temp_goe
        print(f"Temp Score: {temp_score}\n")

        elements_score.append(temp_score)
    
    total_tes = sum(elements_score)
    return round(total_tes, 1)

elements = [
  ("Triple Flip",            9.7,  [3, 2, 3, 3, 2, 4, 3, 2, 3]),
  ("Triple Lutz+Toe Combo", 12.5,  [4, 5, 4, 5, 5, 4, 4, 3, 4]),
  ("Triple Salchow",         7.0,  [2, 3, 2, 2, 3, 2, 2, 3, 2]),
  ("Triple Loop",            6.0,  [3, 3, 2, 4, 3, 3, 2, 3, 2]),
  ("Step Sequence",          3.3,  [4, 4, 4, 4, 3, 3, 4, 3, 4])
]

br_line = "--------------------------\n"

elementsCheck = calculate_score(elements)
print(f"Score = {elementsCheck}")
print(br_line)

elements2 = [("Triple Flip", 9.7, [3, 2, 3, 3, 2, 4, 3, 2, 3]), ("Triple Lutz+Toe Combo", 12.5, [4, 5, 4, 5, 5, 4, 4, 3, 4]), ("Triple Salchow", 7.0, [2, 3, 2, 2, 3, 2, 2, 3, 2]), ("Triple Loop", 6.0, [3, 3, 2, 4, 3, 3, 2, 3, 2]), ("Step Sequence", 3.3, [4, 4, 4, 4, 3, 3, 4, 3, 4])]
             
elements2Check = calculate_score(elements2)
print(f"Score = {elements2Check}")
print(br_line)

elements3 = [ ("Triple Loop+Flip Combo", 13.0, [5, 5, 4, 5, 4, 5, 4, 4, 5]), ("Double Axel", 8.0, [3, 2, 3, 3, 3, 2, 3, 2, 3]), ("Flying Sit Spin", 3.6, [4, 4, 5, 4, 4, 5, 4, 4, 4]), ("Step Sequence", 3.3, [3, 4, 3, 3, 4, 3, 4, 3, 3]), ("Choreographic Sequence", 2.7, [4, 3, 3, 3, 3, 3, 3, 4, 3]), ]

elements3Check = calculate_score(elements3)
print(f"Score = {elements3Check}")
print(br_line)