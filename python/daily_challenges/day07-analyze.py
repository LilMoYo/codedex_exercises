def analyze(percentages): #finishing boilerplate
    years = len(percentages)
    net_change_per_year = 0
    first_3year_avg = 0
    last_3year_avg = 0
    trend = ""
    dips = 0
  
    net_change_per_year = round((percentages[years-1] - percentages[0])/(years-1),4)
    first_3year_avg = round(sum(percentages[:3])/3,4)
    last_3year_avg = round(sum(percentages[-3:])/3,4)
  
    if last_3year_avg > first_3year_avg:
        trend = "improving"
    elif last_3year_avg == first_3year_avg:
        trend = "stagnating"
    else:
        trend = "declining"
        
    for i in range(years):
        if percentages[i] < percentages[i-1]:
            if percentages[i-1] == percentages[-1]:
                dips += 0
            else:
                dips += 1
            print(f"Dips: {dips}")
        print(f"counter: {i}")
  
    print(f"Years: {years}")
    print(f"Net Change Per Year: {net_change_per_year}")
    print(f"First 3 Year Average: {first_3year_avg}")
    print(f"Last 3 Year Average: {last_3year_avg}")
    
    return net_change_per_year, trend, dips


br_line = "--------------------------\n"

# Meta 🌀 (2014-2022)
input1 = [31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]

# Amazon 📦 (2014-2024)
input2 = [42.0, 43.0, 42.0, 43.0, 44.0, 44.0, 44.6, 44.8, 44.7, 45.0, 45.8]

# Apple 🍎 (2014–2024)
input3 = [30.0, 31.0, 32.0, 32.0, 33.0, 34.0, 34.0, 34.8, 35.0, 35.0, 35.3]

# Test Case 4
input4 = [44.0, 45.0, 46.0, 47.3, 47.1, 47.6, 49.8, 51.7, 49.6]
             
inputCheck1 = analyze(input1)
print(f"{inputCheck1}")
print(br_line)

inputCheck2 = analyze(input2)
print(f"{inputCheck2}")
print(br_line)

inputCheck3 = analyze(input3)
print(f"{inputCheck3}")
print(br_line)

inputCheck4 = analyze(input4)
print(f"{inputCheck4}")
print(br_line)