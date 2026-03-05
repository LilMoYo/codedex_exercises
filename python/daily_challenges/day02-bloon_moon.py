def blood_moon(time):
    h, m = map(int, time.split(":"))
    total_minutes = h * 60 + m
    interval = 168
    
    results = []
    
    for _ in range(3):
        total_minutes += interval
        # Keep it within 24 hours (1440 minutes)
        day_minutes = total_minutes % 1440
        
        # Format back to HH:MM
        new_h = day_minutes // 60
        new_m = day_minutes % 60
        results.append(f"{new_h:02d}:{new_m:02d}")
    
    return results

timestamp = input("Enter the time: (24H Format HH:MM) ")
prediction = blood_moon(timestamp)
print(prediction)