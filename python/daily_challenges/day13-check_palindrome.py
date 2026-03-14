import math
def cut_pie(diameter, friends):
    pii = math.pi
    circumference = pii * diameter
    print(circumference)
    
    cut_perfriend = circumference / friends
    print(f"Cut per friend: {cut_perfriend} inch")
    
    return round(cut_perfriend,2)
    
br_line = "--------------------------\n"

# C=π×d
# C = circumference
# d = diameter of the pie

input1_diameter = 10
input1_friends = 8

result1 = cut_pie(input1_diameter, input1_friends)
print(f"Output: {result1}")
print(br_line)


input2_diameter = 12
input2_friends = 5

result2 = cut_pie(input2_diameter, input2_friends)
print(f"Output: {result2}")
print(br_line)


input3_diameter = 15
input3_friends = 9

result3 = cut_pie(input3_diameter, input3_friends)
print(f"Output: {result3}")
print(br_line)


input4_diameter = 10
input4_friends = 8

result4 = cut_pie(input4_diameter, input4_friends)
print(f"Output: {result4}")
print(br_line)
