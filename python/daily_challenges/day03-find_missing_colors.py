def find_missing_colors(grid):
    check_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    missing_colors = []
    gridset = set()
    
    for row in grid:
        gridset.update(row)
        
    for color in check_colors:
        print(f"Color: {color}")
            
        if color not in gridset:
            missing_colors.append(color)
                
    return missing_colors
    
holi = [["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
  ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
  ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
  ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
  ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
  ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
  ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]

holi_check = find_missing_colors(holi)
print(holi_check)

holi2 = [["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟧"],     
["🟨", "🟩", "🟦", "🟥", "🟨", "🟩", "🟦"],     
["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟨"],     
["🟩", "🟦", "🟥", "🟧", "🟨", "🟩", "🟦"],     
["🟨", "🟥", "🟧", "🟨", "🟩", "🟦", "🟥"],     
["🟦", "🟩", "🟨", "🟥", "🟧", "🟩", "🟦"],    
["🟥", "🟧", "🟨", "🟩", "🟦", "🟨", "🟥"]]

holi_check2 = find_missing_colors(holi2)
print(holi_check2)

holi3 = [["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"],
  ["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"],
  ["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"],
  ["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"],
  ["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"],
  ["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"],
  ["🟪", "🟪", "🟪", "🟪", "🟪", "🟪", "🟪"]]

holi_check3 = find_missing_colors(holi3)
print(holi_check3)